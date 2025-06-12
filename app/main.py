from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import app.schemas as schemas
from dotenv import load_dotenv



app = FastAPI()

#load_dotenv()





# What we need for building CRUD
# Database, FastAPI, Pycopg

@app.get("/")
def intro():
    return {"message": "It works"}







    