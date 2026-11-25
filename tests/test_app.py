
from app import app

# Test 1: Check whether the home page works
def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data.decode() == "Welcome to our DevOps CI/CD Project!"


# Test 2: Check whether an invalid URL returns 404
def test_invalid_page():
    client = app.test_client()
    response = client.get("/invalid")

    assert response.status_code == 404
