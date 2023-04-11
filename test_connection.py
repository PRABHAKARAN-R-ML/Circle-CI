import pytest 
import requests
def test_connection():
    url = "http://localhost:5000/data/create"
    response= requests.get(url=url)
    assert response.status_code == 200
