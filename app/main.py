from fastapi import FastAPI, File, UploadFile
from app.schemas import Image
from dotenv import load_dotenv

from random import randrange


app = FastAPI()

#load_dotenv()



my_images = [{"title": "title of image 1", "content": "content of image 1", "id": 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]

# What we need for building CRUD
# Database, FastAPI, Pycopg

@app.get("/")
def root():
    return {"message": "It works"}

@app.get("/images")
def get_images():
    return {"data": my_images}



@app.post("/images")
def create_images(image: Image):
    # Take the new_image and store it in the database. Then, return the new image with the id as a dict
    image_dict = image.dict()
    image_dict['id'] = randrange(0,1000000)
    return image_dict



@app.put("/images/{id}")
def update_images(id: int, image: Image):
    # find the image with the matching id

    for i, item in enumerate(my_images):
        if(item['id'] == id):
            updated_image = image.dict() # Create a dict representation first, separately to do multiple operations on (and make cleaner)
            updated_image['id'] = id    # Safely insert id
            my_images[i] = updated_image # Finally, set the array index to the updated image
            return updated_image
    
    return {"error": "Image not found"}
    # manipulate the image
    # return the updated image as a dictionary






    