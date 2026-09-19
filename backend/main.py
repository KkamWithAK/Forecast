import requests
from dotenv import load_dotenv
import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}