from fastapi import FastAPI
from services.data_loader.db import DataLoader
import os

app = FastAPI()

loader = DataLoader(
    host=os.environ.get("MYSQL_HOST", "localhost"),
    user=os.environ.get("MYSQL_USER", "user"),
    password=os.environ.get("MYSQL_PASSWORD", "password"),
    database=os.environ.get("MYSQL_DATABASE", "mydb")
)


@app.get("/data")
def read_data():

    return loader.get_all_data()