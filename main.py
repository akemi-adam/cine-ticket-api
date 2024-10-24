from typing import Union

from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get('/')
def home():
    return {
        'title': 'teste'
    }