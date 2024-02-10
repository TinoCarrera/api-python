from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}

@app.get("/suma")
def suma(a: Union[int, None] = None, b: Union[int, None] = None):
    if a and b:
        result = {"result": a + b}
    else:
        result = {"message": "Debes enviar los parámetros 'a' y 'b' con los números a sumar"}

    return result

@app.get("/resta")
def resta(a: Union[int, None] = None, b: Union[int, None] = None):
    if a and b:
        result = {"result": a - b}
    else:
        result = {"message": "Debes enviar los parámetros 'a' y 'b' con los números a restar"}

    return result

@app.get("/multiplicacion")
def multiplicacion(a: Union[int, None] = None, b: Union[int, None] = None):
    if a and b:
        result = {"result": a * b}
    else:
        result = {"message": "Debes enviar los parámetros 'a' y 'b' con los números a multiplicar"}

    return result

@app.get("/division")
def division(a: Union[int, None] = None, b: Union[int, None] = None):
    if b == 0:
        result = {"message": "No se puede dividir entre cero"}
    elif a and b:
        result = {"result": a / b}
    else:
        result = {"message": "Debes enviar los parámetros 'a' y 'b' con los números a dividir"}

    return result
