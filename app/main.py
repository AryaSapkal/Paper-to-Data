from fastapi import FastAPI, File, HTTPException, UploadFile
from app.schemas import Image
from dotenv import load_dotenv
from datetime import datetime

from random import randrange

import psycopg2
from psycopg2.extras import RealDictCursor

import os


app = FastAPI()

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")



try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cur = conn.cursor()
    print("Connection successful")
except Exception as e:
    print("Connection failed")
    print(f"Error: {e}")











my_images = [{"title": "title of image 1", "content": "content of image 1", "id": 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]


@app.get("/")
def root():
    return {"message": "It works"}

@app.get("/images")
def get_images():
    cur.execute("""SELECT * FROM images""")

    images = cur.fetchall()
    return {"data": images}



@app.post("/images")
def create_images(image: Image):
    # Take the new_image and store it in the database. Then, return the new image with the id as a dict
    image_dict = image.dict()
    filename = image_dict['filename']
    content = image_dict['content']
    time_created = image_dict['time_created']
    rating = image_dict['rating']

    cur.execute("""INSERT INTO images (filename, content, time_created, rating) 
                VALUES (%s, %s, %s, %s)
                RETURNING id""",(filename, content, time_created, rating))
    
    conn.commit()
    return {"data": image_dict}
    


# Update an image
@app.put("/images/{id}")
def update_images(id: int, image: Image):

    cur.execute("""UPDATE images SET filename = %s, content = %s, rating=%s
                WHERE id = %s RETURNING *""", (image.filename, image.content, image.rating, str(id)))

    updated_image = cur.fetchone()
    conn.commit()

    if not updated_image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    return updated_image
    




# Get one individual image
@app.get("/images/{id}")
def get_image(id: int):
    cur.execute("""SELECT * FROM images WHERE id=%s""", (str(id),))
    image_retrieved = cur.fetchall()
    #conn.commit()

    if not image_retrieved:
        raise HTTPException(status_code=404, detail="Image not found")
    
    return image_retrieved


# Delete an image
@app.delete("/images/{id}")
def delete_images(id: int):

    cur.execute("""DELETE FROM images
                WHERE id = %s RETURNING *""", (str(id),))
    
    deleted_post = cur.fetchone()
    conn.commit()

    if not deleted_post:
        raise HTTPException(status_code=404, detail="Image not found")
    
    return {"data": "image removed"}



# Accept a file from the user
app.post("/files")
def upload_image(file: UploadFile):
    print("Uploaded filename:", file.filename)

    file_dict = file.dict()
    filename = file.filename
    content_type = file_dict['content_type']
    fileObject = file_dict['file']


    cur.execute("""INSERT INTO image (filename, content)
                    VALUES (%s, %s) RETURNING *""", (filename, fileObject))
    


    conn.commit()

    return {"data": file_dict}



    