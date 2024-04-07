# Planetary API

Planetary API is a simple RESTful API built using Flask and SQLAlchemy for managing information about planets and users.


## Features

1. User Management: Allows registration and login functionalities for users.

2. Planet Information: Provides CRUD operations for managing planetary data such as planet name, type, and attributes.

3. Authentication: Utilizes JWT (JSON Web Tokens) for secure authentication of users.


## Installation

### 1. Clone the repository:

``` git clone https://github.com/yourusername/planetary-api.git```

### 2. Set up environment variables:

```MAIL_USERNAME: Your SMTP username for sending emails.```

```MAIL_PASSWORD: Your SMTP password for sending emails.```


### 3. Initialize the database:
```flask db_create```

### 4. Seed the database with sample data:
```flask db_seed```

### 5. Run the application:
```flask run```

The API will be accessible at http://localhost:5000.

# Endpoints
GET /planets: Retrieve a list of all planets.

POST /register: Register a new user.

POST /login: Authenticate a user and generate an access token.

GET /retrieve_password/<email>: Retrieve password for a user via email.

GET /planet_details/<planet_id>: Retrieve details of a specific planet.

POST /add_planet: Add a new planet (requires authentication).

PUT /update_planet: Update details of an existing planet (requires authentication).

DELETE /remove_planet/<planet_id>: Delete a planet (requires authentication).

