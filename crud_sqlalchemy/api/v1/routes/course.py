from typing import List

from core.deps import get_session
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from models.course import Course
from schemas.course_schemas import CourseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from repository.sqlalchemy.course import SqlAlchemyCourseRepository

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CourseSchema)
async def create_course(curso: CourseSchema, db: AsyncSession = Depends(get_session)) -> CourseSchema:
    course = SqlAlchemyCourseRepository()
    course = course.post(course=curso)

    db.add(course)
    await db.commit()

    return course


@router.get("/", response_model=List[CourseSchema])
async def show_courses(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Course)
        result = await session.execute(query)
        courses: List[Course] = result.scalars().all()

        return courses


@router.get('/{course_id', response_model=CourseSchema, status_code=status.HTTP_200_OK)
async def search_course(course_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Course).filter(Course.id == course_id)
        result = await session.execute(query)
        course = result.scalar_one_or_none()

        if course:
            return course
        else:
            raise HTTPException(detail='Curso nao encontrado.', status_code=status.HTTP_404_NOT_FOUND)
