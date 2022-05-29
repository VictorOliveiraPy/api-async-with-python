from sqlalchemy import Column, Integer, String

from core.config import settings


class Course(settings.DBBaseModel):
    __tablename__: str = 'courses'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100))
    classes: int = Column(Integer)
    hours: int = Column(Integer)
