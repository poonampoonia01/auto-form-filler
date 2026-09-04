from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import boto3

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close    

def get_s3_client():
    session = boto3.session.Session(
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        region_name=settings.aws_region,
    )

    client_kwargs = {}
    if getattr(settings, "s3_endpoint", None):
        client_kwargs["endpoint_url"] = settings.s3_endpoint
    if getattr(settings, "s3_force_path_style", False):
        client_kwargs["config"] = boto3.session.Config(s3={'addressing_style': 'path'})

    return session.client("s3", **client_kwargs)