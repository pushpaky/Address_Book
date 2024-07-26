# Address Book API

This is an Address Book API built with FastAPI and SQLite.

## Features

- Create, update, delete addresses
- Addresses contain coordinates
- Retrieve addresses within a given distance from specified coordinates
- Input validation
- Logging
- Exception handling
- Docker support

## Endpoints

- `POST /addresses/`: Create a new address
- `GET /addresses/{address_id}`: Get an address by ID
- `PUT /addresses/{address_id}`: Update an address by ID
- `DELETE /addresses/{address_id}`: Delete an address by ID
- `GET /addresses/`: Get addresses within a given distance from specified coordinates

## Running the Application

To run the application with Docker:

```bash
docker build -t address-book-api .
docker run -d -p 8000:8000 address-book-api
