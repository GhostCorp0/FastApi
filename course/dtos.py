from pydantic import BaseModel
from fastapi import FastAPI

class ProductDTO(BaseModel):
    id:int
    title:str
    price:int = 0
    count:int = 0