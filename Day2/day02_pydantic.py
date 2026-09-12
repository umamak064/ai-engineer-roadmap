from pydantic import BaseModel, ConfigDict,Field

# class User(BaseModel):
#     id:int
#     name:str="john dae"

#     model_config= ConfigDict(str_max_length=12)

# user= User(id=1234)    
# print(user)

# PRACTICE
# 1. Create a Book model with title: str , author: str , year: int .
# 2. Try creating a Book with year="not a number" — read the error message carefully.


class Book(BaseModel):
    title:str
    author:str
    year:int

book=Book(title="14 rules", author="elif shafak", year="abds") 
print(book)   

# 3. Create a Product model with name: str , price: float , in_stock: bool = True (default value).
# 4. Add a constraint: price must be greater than 0 (use Field(gt=0) )

class Product(BaseModel):
    name:str
    price:float=Field(gt=0)
    in_stock:bool=True 

product=Product(name="cover", price=100)    
print(product)

