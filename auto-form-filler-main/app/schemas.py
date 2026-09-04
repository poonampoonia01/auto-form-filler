from pydantic import BaseModel

class PhotoBase(BaseModel):
    photo_name: str
    photo_url: str
    is_deleted: bool = False

class PhotoCreate(BaseModel):
    photo_name: str

class Photo(PhotoBase):
    id: int

    class Config:
        from_attributes = True