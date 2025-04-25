# MyBazar API

Django REST API backend for MyBazar e-commerce platform.

## Requirements

- Docker and Docker Compose

## Development

To run the project in development mode:

```bash
make run
```
Default admin user:
- username: admin
- password: admin

This will:
- Build the Docker image
- Run database migrations
- Load sample data
- Start the Django development server on port 8000

You can access the API at http://localhost:8000/

## Testing

To run tests:

```bash
make test
```

This will:
- Build the Docker image
- Run database migrations
- Execute pytest tests

## Project Structure

- `app/` - Django application code
- `tests/` - Test files
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker Compose configuration for development
- `docker-compose.test.yml` - Docker Compose configuration for testing
