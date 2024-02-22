# Hero API

This is a Python-based API for managing heroes. The API is built using FastAPI and SQLAlchemy.

## Project Structure

The project is organized as follows:

- [`main.py`](main.py): This is the main module of the API. It contains the FastAPI application and all the route handlers.
- [`src/`](src/): This directory contains the source code of the application.
  - [`crud.py`](src\crud.py): This module contains the CRUD (Create, Read, Update, Delete) operations for the [`Hero`](src/models.py) model.
  - [`models.py`](src\models.py): This module contains the SQLAlchemy models of the application.
  - [`schemas.py`](src\schemas.py): This module defines the Pydantic schemas of the application.

## API Endpoints

The API provides the following endpoints:

- `GET /`: Returns all heroes.
- `POST /`: Creates a new hero. The request body should be a JSON object that matches the [`HeroSchemaIn`](src/schemas.py) schema.
- `DELETE /{hero_id}`: Deletes a hero by ID.
- `GET /{hero_id}`: Returns a hero by ID.
- `PUT /{hero_id}`: Levels up a hero by ID.

## Models

The application defines the following models:

- [`Hero`](src/models.py): Represents a hero. Each hero has an ID, a name, a class, and a level.

## Schemas

The application defines the following schemas:

- [`HeroSchemaIn`](src/schemas.py): Represents the data required to create a new hero. It includes the name and class of the hero.

## Installation

To install the project, you need to have Python installed on your machine. Then, you can install the project dependencies using pip:

```powershell
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command:

```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.
