This repository contains a FastAPI application developed as part of the Nimap Machine Test. The application is containerized using Docker and ensures data persistence with a JSON file.

Introduction
This project is a FastAPI-based web application designed for a machine test at Nimap. It demonstrates the use of Docker for containerization and manages data persistence using a JSON file stored within a Docker volume.

Features

FastAPI Framework: Efficient and easy-to-use web framework for building APIs.
Dockerized: Containerized application for consistent development and deployment environments.
Persistent Data Storage: Data is stored in a JSON file and remains persistent across container restarts.
RESTful API: Provides endpoints to manage user data.
Project Structure

│
├── data/                 # Directory for persistent data storage
├── app/
│   ├── __init__.py       # Application module initialization
│   ├── main.py           # Main FastAPI application file
│
├── Dockerfile            # Instructions to build the Docker image
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
└── .gitignore            # Files and directories to ignore in Git
Getting Started
Prerequisites
Docker: Ensure Docker is installed on your machine. You can download it from Docker's official website.
Docker Compose: Docker Compose is typically included with Docker Desktop on Windows and Mac. On Linux, you may need to install it separately. Check Docker Compose installation guide.
Installation
Clone the Repository:
git clone https://github.com/sujatab05/Nimap_MachineTest.git
cd Nimap_MachineTest
Create a data Directory:

This directory will be used to store persistent data.
mkdir data
Running the Application
Build and Start the Application:

Use Docker Compose to build and run the application.

docker-compose up --build
Access the Application:

The application will be available at http://localhost:8000.

API Documentation:

FastAPI provides interactive API documentation at http://localhost:8000/docs.

Stopping the Application
To stop the application, use:

docker-compose down
This command stops and removes the Docker containers created by Docker Compose.

API Endpoints
The following endpoints are available:

GET /: Returns a welcome message.
GET /users: Retrieves the list of users.
POST /users: Adds a new user. The request body should be a JSON object with the following structure:


Testing
You can test the API endpoints using various tools:

Swagger UI: Navigate to http://localhost:8000/docs for an interactive API interface.

