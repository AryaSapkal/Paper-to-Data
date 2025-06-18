from fastapi import FastAPI, File, HTTPException, UploadFile
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
    my_images.append(image_dict)
    return image_dict



@app.put("/images/{id}")
def update_images(id: int, image: Image):

    # find the image of id id in the array
    for i, item in enumerate(my_images):
        if item['id'] == id:
            updated_image = image.dict() # needs to be a dict representation of the image parameter, not the item (this wouldn't make use of what we want/passing in)
            updated_image['id'] = id # keep the id of the image the same
            my_images[i] = updated_image
            return updated_image

        
    
    
    raise HTTPException(status_code=404, detail="Image not found")


    # create an updated_image object and add


# Get one individual image
@app.get("/images/{id}")
def get_image(id: int):
    for i, item in enumerate(my_images):
        if item['id'] == id:
            return item
        
    raise HTTPException(status_code=404, detail="Image not found")

@app.delete("/images/{id}")
def delete_images(id: int):

    for i, item in enumerate(my_images):
        if item['id'] == id:
            my_images.remove(item)
            return {"data": "image removed"}

    
    raise HTTPException(status_code=404, detail="Image not found")





    