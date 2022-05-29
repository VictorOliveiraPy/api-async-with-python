from pydantic import BaseModel, validator

courses = {
    1: {
        "title": "Programacao para Leigos",
        "classes": 112,
        "hours": 58
    },
    2: {
        "title": "Algoritmos e Logica de Programacao",
        "classes": 112,
        "hours": 58
    }
}


class Course(BaseModel):
    id: int
    title: str
    classes: int
    hours: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras')
        return value
