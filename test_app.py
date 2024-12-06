# Importing the 'app' object from the 'app' module, which is assumed to be the Flask application
from app import app

# Defining a test function for the home route ("/")
def test_home():
    # Using Flask's test_client() to simulate a GET request to the home page ("/")
    response = app.test_client().get("/")

    # Asserting that the response status code is 200 (OK), which indicates the request was successful
    assert response.status_code == 200

    # Asserting that the response data is equal to the expected byte string "Hello World!"
    assert response.data == b"Hello World!"
