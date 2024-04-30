from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Flask application' in response.data  # Adjust this based on your index.html content

def test_index_route_post_valid_credentials(client):
    data = {'name': 'omar', 'password': '2222'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Logged In horai' in response.data  # Adjust this based on your loged_in.html content

