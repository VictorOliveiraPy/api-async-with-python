from typing import Optional, Any, Dict

from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi import status
from fastapi import Path
from fastapi import Header
from fastapi import Depends

from time import sleep

from models import Course, courses


def fake_db():
    try:
        print("Abrindo conexao com o banco de dados...")
        sleep(1)
    finally:
        print("Fechado conexao com banco de dados...")
        sleep(1)


app = FastAPI(
    title='API do Victor',
    version='0.0.1',
    description='api para estudos'
)


@app.get("/cursos", description="Retorna todos os cursos", summary="Retorna todos os cursos", response_model=Dict[int, Course])
async def get_course(db: Any = Depends(fake_db)):
    return courses


@app.get("/cursos/{curso_id}")
async def get_course(
        curso_id: int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3, ),
        db: Any = Depends(fake_db)):
    try:
        course = courses[curso_id]
        return course
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID nao encontrado.')


@app.post("/cursos")
async def create_course(curso: Course, db: Any = Depends(fake_db)):
    next_id: int = len(courses) + 1
    courses[next_id] = curso
    return curso


@app.get("/calculadora")
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10, ),
                   x_geek: str = Header(default=None), c: Optional[int] = None, db: Any = Depends(fake_db)):
    result = a + b + c
    return {"resultado": result, "header": x_geek}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
