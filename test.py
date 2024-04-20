import pytest
from app import app, db, Planet, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

def test_register_and_login(client):
    # Register a user
    response = client.post('/register', data=dict(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        password='password'
    ))
    assert response.status_code == 201

    # Login with registered user
    response = client.post('/login', data=dict(
        email='john@example.com',
        password='password'
    ))
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_planets_endpoint(client):
    # Add some planets to the database
    mercury = Planet(planet_name='Mercury', planet_type='Class D', home_star='Sol', mass=2.258e23, radius=1516, distance=35.98e6)
    db.session.add(mercury)
    db.session.commit()

    # Make a request to the /planets endpoint
    response = client.get('/planets')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['planet_name'] == 'Mercury'
