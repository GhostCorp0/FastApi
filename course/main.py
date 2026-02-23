from fastapi import FastAPI, Request
from mockdata import products
from dtos import ProductDTO

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
        "error": "Product not found for this id"
    }


# Query parameters
@app.get("/greet")
def greet_user(name: str, age: int):
    return {
        "greet": f"Hello {name},How are  you? Your age is {age}"
    }


# n numbers of Query Parameters
@app.get("/requestBody")
def request_body(request: Request):
    query_params = dict(request)
    return {
        "greet": f"Hello {query_params.get('name')} , Your age is {query_params.get('age')}"
    }


# Different types of http methods
# How to validate data DTOs
# How to call different HTTP Methods.

# PUT #POST #PATCH #GET #DELETE

## body,headers -- request header, params

# pydentic is a module

## To create a post method
@app.post("/create_product")
def create_product(body: ProductDTO):
    product_data = body.model_dump()
    products.append(product_data)
    return {"status": "Product Crated Successfully...", "data": products}


## to update object
@app.put("/update_product")
def update_product(product_data: ProductDTO, product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "Product Updated Successfully...", "Product": product_data}

    return {
        "error": "Product not Found for this ID."
    }


## to delete

@app.delete("/delete_product")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status": "Product Deleted Successfully...", "product": deleted_product}

    return {
        "error": "Product not Found for this  ID."
    }