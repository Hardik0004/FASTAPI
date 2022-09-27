from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello Fastapi"}


class calculator(BaseModel):
    a: int
    b: int


@app.post("/calculator/sum")
def calculator_addition(cal: calculator):
    response = cal.dict()
    num_1 = response.get("a", 0)
    num_2 = response.get("b", 0)
    sum_1 = num_1+num_2
    return {"Answer": sum_1}


@app.post("/calculator/subtraction_number")
def calculator_subtraction(cal: calculator):
    response = cal.dict()
    num_1 = response.get("a", 0)
    num_2 = response.get("b", 0)
    Subtraction_1 = num_1-num_2
    return {"Answer": Subtraction_1}


@app.post("/calculator/multipication_number")
def calculator_multipication(cal: calculator):
    response = cal.dict()
    num_1 = response.get("a", 0)
    num_2 = response.get("b", 0)
    multipication_1 = num_1*num_2
    return {"Answer": multipication_1}


@app.post("/calculator/divison_number")
def calculator_divison(cal: calculator):
    response = cal.dict()
    num_1 = response.get("a", 0)
    num_2 = response.get("b", 0)
    try:
        Divison_1 = num_1/num_2
        return {"Answer": Divison_1}
    except:
        return {"Not divided by zero"}
