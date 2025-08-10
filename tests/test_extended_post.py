import pytest
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def test_post_extended():
    payload = {
  "title": "Advanced test title",
  "body": "This body contains more detailed information and multiple lines.",
  "userId": 123,
  "tags": ["testing", "api", "post"],
  "metadata": {
    "timestamp": "2025-08-10T12:00:00Z",
    "priority": "high"
  }
    }

    response = requests.post(url, json=payload)
    data = response.json()

    assert response.status_code == 201
    keys = ["id", "title", "body", "userId", "tags", "metadata"]
    for key in keys:
        assert key in data
    
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["tags"] == payload["tags"]
    assert data["metadata"] == payload["metadata"]

    assert isinstance(data["id"], int)
    
