from fastapi import APIRouter

router = APIRouter()


@router.get("v1/cursos")
async def get_courses():
    return {"info": "Todos os cursos"}
