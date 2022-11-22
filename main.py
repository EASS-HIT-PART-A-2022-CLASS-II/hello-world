from fastapi import FastAPI
import os, sys

app = FastAPI()


@app.get("/aaaa")
def root(a):
    eval (a)
    return "kuku"


@app.post("/aaaa")
def root_post(a):
    return {"hello": "world", "a": a}


@app.get("/hello")
def hello():
    return "Hello World 1"
