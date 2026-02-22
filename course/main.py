from fastapi import FastAPI,Request
from mockdata import products

app = FastAPI()


# api examples
@app.get("/")
def home():
    return "Welcome to FastAPI Series !"


@app.get("/products")
def get_products():
    return products


# Path Params Examples
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    ## if product available with the id,return product else return error message
    product = None
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct

    return {
        "error":"Product not found for this id"
    }

#Query parameters
@app.get("/greet")
def greet_user(name:str,age:int):
    return {
        "greet": f"Hello {name},How are  you? Your age is {age}"
    }

# n numbers of Query Parameters
@app.get("/requestBody")
def request_body(request:Request):
    query_params = dict(request.query_params)
    return {
        "greet": f"Hello {query_params.get('name')} , Your age is {query_params.get('age')}"
    }

#Different http methods


