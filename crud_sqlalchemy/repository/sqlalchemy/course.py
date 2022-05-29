from abc import ABC
from sqlalchemy.orm import Session

from repository.sqlalchemy.abstract import AbstractRepository

from schemas.course_schemas import CourseSchema

from models.course import Course


class SqlAlchemyCourseRepository(AbstractRepository, ABC):

    def post(self, course: CourseSchema, db: Session):
        course = Course(**course.dict())

        db.add(course)
        db.commit()
        db.refresh(course)
        return course
