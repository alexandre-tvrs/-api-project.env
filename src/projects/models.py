from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base


class Project(Base):
    __tablename__ = "projects"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, unique=True, index=True, nullable=False)
    description: str = Column(String, index=True, nullable=True)
    icon: str = Column(String, index=True, nullable=True)