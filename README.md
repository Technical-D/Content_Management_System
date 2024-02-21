# CMS Project

This project is a Content Management System (CMS) built using Django and Django REST Framework. It provides API endpoints for user registration, user authentication, and managing content.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/cms-project.git
cd cms-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply database migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

### User Registration

- Endpoint: `/api/register/`
- Method: POST
- Description: Allows users to register with the CMS by providing their email and password.

### User Login

- Endpoint: `/api/login/`
- Method: POST
- Description: Allows registered users to log in to the CMS by providing their email and password.

### Content List

- Endpoint: `/api/content/`
- Method: GET, POST
- Description: Allows authenticated users to retrieve a list of content items or create a new content item.

### Content Detail

- Endpoint: `/api/content/<int:pk>/`
- Method: GET, PUT, DELETE
- Description: Allows authenticated users to retrieve, update, or delete a specific content item identified by its primary key.

## Authentication

- Token-based authentication is used to authenticate users for accessing protected API endpoints.
- To access protected endpoints, clients must include an authentication token in the `Authorization` header of the HTTP request. The token should be prefixed with the string "Token", followed by a space, and then the token value.
- Example header: `Authorization: Token <your-token-value>`

## Permissions

- Users can only create, view, update, or delete content items that they have created.
- Admin users have permission to perform CRUD operations on all content items.

## Testing

- Automated tests for the API endpoints are located in the `tests.py` file.
- Run the tests using the following command:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
