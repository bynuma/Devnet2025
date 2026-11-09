from fastapi import FastAPI             # The FastAPI class is imported from the fastapi module to create a FastAPI application instance.
from pydantic import BaseModel          # The BaseModel class is imported from the pydantic module to define data models for request and response validation.

app = FastAPI(title="Simple API")       # An instance of the FastAPI class is created with the title "Simple API". This instance will be used to define routes and handle requests.

class Item(BaseModel):                  # A data model named Item is defined by inheriting from BaseModel. This model will be used to validate the request body for the /items/ endpoint.
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")                                           # The @app.get("/") decorator defines a GET endpoint at the root URL ("/"). When a GET request is made to this URL, the read_root function will be executed.
async def read_root():                                  # The read_root function is defined as an asynchronous function that returns a JSON response with a welcome message.
    return {"message": "Welcome to the Simple API"}     # The function returns a dictionary that will be automatically converted to JSON format by FastAPI.

@app.post("/items/")                                                        # The @app.post("/items/") decorator defines a POST endpoint at the URL "/items/". When a POST request is made to this URL, the create_item function will be executed.
async def create_item(item: Item):                                          # The create_item function is defined as an asynchronous function that takes an item parameter of type Item. FastAPI will automatically validate the request body against the Item model and convert it to an instance of the Item class.
    return {"item": item, "total_price": item.price + (item.tax or 0)}      # The function returns a dictionary containing the item data and the total price, which is calculated by adding the item's price and tax (if provided). If tax is not provided, it defaults to 0. FastAPI will automatically convert this dictionary to JSON format for the response.