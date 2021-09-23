from uuid import uuid4

from sqlalchemy import Column, String

from weesh.database.database import Base

class URL(Base):
    __tablename__ = "urls"
    
    id = Column(String, primary_key=True, unique=True, default=lambda : str(uuid4().hex))
    url = Column(String)
