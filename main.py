from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from . import schemas
from dotenv import load_dotenv
import os
import psycopg
from psycopg.rows import dictrow
import time


app = FastAPI()

load_dotenv()


# Connect the DB with hidden variables
while True:
    try:
        conn = psycopg.connect(host = os.getenv("DB_HOST"), dbname = os.getenv("DB_NAME"), user = os.getenv("DB_USER"), password = os.getenv("DB_PASSWORD"), row_factory = dict_row)
        cursor = conn.cursor()
        print("DB connection successful")
        break
    except Exception as error:
        print("DB connection failed")
        print("Error: ", error)
        time.sleep(2)


# What we need for building CRUD
# Database, FastAPI, Pycopg






    