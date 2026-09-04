from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, index=True)
    photo_name = Column(String, nullable=False)
    photo_url = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)