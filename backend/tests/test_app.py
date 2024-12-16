import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Тест основного эндпоинта API"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}
