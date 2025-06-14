from fastapi import FastAPI, File, UploadFile
from app.schemas import Image
from dotenv import load_dotenv



app = FastAPI()

#load_dotenv()





# What we need for building CRUD
# Database, FastAPI, Pycopg

@app.get("/")
def root():
    return {"message": "It works"}

@app.get("/images")
def get_images():
    return {"data": "This are your images"}



@app.post("/createimages")
def create_images(new_image: Image):
    print(new_image)
    return {"data": "new image"}





    