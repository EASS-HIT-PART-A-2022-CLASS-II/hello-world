from fastapi import FastAPI
import os, sys

app = FastAPI()


@app.post("hello")
def hello_post(a):
    return {"hello": "world", "a": a}


@app.get("/hello")
def hello():
    return "Hello World 1"
