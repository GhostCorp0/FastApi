from fastapi import FastAPI
from mockdata import products

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"

@app.get("/products")
def get_products():
    return products
