from fastapi import FastAPI, UploadFile, File, Depends, status
from .database import get_db, engine, get_s3_client
from sqlalchemy.orm import Session
from . import models, schemas
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from botocore.exceptions import ClientError, NoCredentialsError
from fastapi import HTTPException
import uuid

app = FastAPI(title="Photo Upload FastAPI")

#origins = ["www.youtube.com", "www.google.com"]
origins=["*"]
#methods = ["GET", "PUT", "POST", "HEAD"]
methods = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message" : "Welcome to my Photo Upload Service API..."}

@app.get("/photos", response_model=List[schemas.Photo])
async def list_photos(db: Session = Depends(get_db)):
    return db.query(models.Photo).order_by(models.Photo.id.desc()).all()

@app.post("/photos", response_model=schemas.Photo, status_code=status.HTTP_201_CREATED)
async def upload_photo(file: UploadFile = File(...), db: Session = Depends(get_db)):
    print("Upload Photo endpoint hit...")
    print(file.filename)
    print(file.content_type)
    
    original_name = file.filename
    ext = ""
    if "." in original_name:
        ext = "." + original_name.rsplit(".", 1)[1]
    key = f"{uuid.uuid4()}{ext}"

    s3 = get_s3_client()
    bucket_name = settings.s3_bucket_name
    
    try:
        s3.upload_fileobj(
            file.file,
            bucket_name,
            key,
            ExtraArgs={"ACL": "public-read", "ContentType": file.content_type or "application/octet-stream"},
        )
    except NoCredentialsError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="AWS credentials not configured on server.")
    except ClientError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"S3 upload failed: {e}")

    uploaded_file_url = f"https://{settings.s3_bucket_name}.s3.amazonaws.com/{key}"
    
    new_photo = models.Photo(photo_name=file.filename, photo_url=uploaded_file_url)
    db.add(new_photo)
    db.commit()
    db.refresh(new_photo)
    return new_photo
