from fastapi.testclient import TestClient               # The TestClient class is imported from the fastapi.testclient module to create a test client for the FastAPI application. This client will be used to send requests to the application during testing.
from main import app                                    # The FastAPI application instance (app) is imported from the main module. This instance will be used to create the test client and send requests to the application during testing.

client = TestClient(app)                                # The TestClient instance is created by passing the FastAPI application instance (app) to it. This client will be used to send requests to the application during testing.

def test_read_root():                                                       # The test_read_root function is defined to test the GET endpoint at the root URL ("/"). This function will send a GET request to the root URL and assert that the response status code is 200 (OK) and that the response JSON matches the expected output.
    response = client.get("/")                                              # The client.get("/") method is called to send a GET request to the root URL ("/") of the FastAPI application. The response from the server is stored in the response variable.
    assert response.status_code == 200                                      # The assert statement checks if the response status code is 200 (OK). If the status code is not 200, an AssertionError will be raised, indicating that the test has failed.
    assert response.json() == {"message": "Welcome to the Simple API"}      # The assert statement checks if the response JSON matches the expected output, which is a dictionary containing the message "Welcome to the Simple API". If the response JSON does not match the expected output, an AssertionError will be raised, indicating that the test has failed.

def test_create_item():                                 # The test_create_item function is defined to test the POST endpoint at the URL "/items/". This function will send a POST request with a JSON payload representing an item and assert that the response status code is 200 (OK) and that the response JSON matches the expected output.
    test_item = {                                       # The test_item dictionary is defined to represent an item with the following attributes: name, description, price, and tax. This dictionary will be sent as a JSON payload in the POST request to the "/items/" endpoint.
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99,
        "tax": 1.99
    }
    response = client.post("/items/", json=test_item)                       # The client.post("/items/", json=test_item) method is called to send a POST request to the URL "/items/" of the FastAPI application. The test_item dictionary is passed as a JSON payload in the request body. The response from the server is stored in the response variable.
    assert response.status_code == 200                                      # The assert statement checks if the response status code is 200 (OK). If the status code is not 200, an AssertionError will be raised, indicating that the test has failed.
    data = response.json()                                                  # The response.json() method is called to parse the response body as JSON and store it in the data variable. This variable will be used to assert that the response JSON matches the expected output.
    assert data["item"]["name"] == test_item["name"]                        # The assert statement checks if the "name" attribute of the item in the response JSON matches the "name" attribute of the test_item dictionary. If they do not match, an AssertionError will be raised, indicating that the test has failed.
    assert data["item"]["price"] == test_item["price"]
    assert data["total_price"] == test_item["price"] + test_item["tax"]

def test_create_item_without_tax():                # The test_create_item_without_tax function is defined to test the POST endpoint at the URL "/items/" without providing a tax value. This function will send a POST request with a JSON payload representing an item without tax and assert that the response status code is 200 (OK) and that the response JSON matches the expected output.
    test_item = {                                  # The test_item dictionary is defined to represent an item with the following attributes: name, description, and price. The tax attribute is omitted to test the behavior of the endpoint when tax is not provided. This dictionary will be sent as a JSON payload in the POST request to the "/items/" endpoint.
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99
    }
    response = client.post("/items/", json=test_item)       # The client.post("/items/", json=test_item) method is called to send a POST request to the URL "/items/" of the FastAPI application. The test_item dictionary is passed as a JSON payload in the request body. The response from the server is stored in the response variable.
    assert response.status_code == 200                      # The assert statement checks if the response status code is 200 (OK). If the status code is not 200, an AssertionError will be raised, indicating that the test has failed.
    data = response.json()                                  # The response.json() method is called to parse the response body as JSON and store it in the data variable. This variable will be used to assert that the response JSON matches the expected output.
    assert data["item"]["name"] == test_item["name"]        # The assert statement checks if the "name" attribute of the item in the response JSON matches the "name" attribute of the test_item dictionary. If they do not match, an AssertionError will be raised, indicating that the test has failed.
    assert data["item"]["price"] == test_item["price"]
    assert data["total_price"] == test_item["price"]

##################
# uvicorn main:app --reload
# The above command is used to run the FastAPI application using Uvicorn, a lightning-fast ASGI server. The `--reload` flag enables auto-reloading of the server when code changes are detected, which is useful during development.
##################
# python3 -m pytest test_app.py -v
# The above command is used to run the tests defined in the `test_app.py` file using pytest, a testing framework for Python. The `-v` flag stands for "verbose" and provides detailed output of the test results, including which tests passed or failed.
##################