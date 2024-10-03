# server_test.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
 return {"color":{"red":0,"green":0,"blue":0}}