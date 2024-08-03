# Docker Tasks

This repo contains code files for 3 Docker tasks described below.

## Table of Contents
-----------------

* [Getting Started](#getting-started)
* [Task 1](#task-1)
* [Task 2](#task-2)
* [Task 3](#task-3)

## Getting Started
---------------

To get started with this repository, simply clone it to your local machine:

```bash
git clone git@github.com:omer-io/docker-tasks.git
```

## Task 1
---------------

**(Installation and basic usage)**
- Install Docker on your local machine and verify that it is running correctly by running the hello-world example.
- Pull and run the official nginx Docker image in detach mode and access the web server from your browser.
- Stop and remove the nginx container.

## Task 2
---------------

**(Building and running a custom Docker image)**
- Create your own docker by creating a custom image that can install the following tools:
    - CMake, Make
    - Python, Python3
    - Git
    - GCC
- Build and run a simple C++ application inside the Dockerfile
- Build your image
- Map your source directory with the container - Volume mapping. (Remember to map your source directory from your user to the Docker's user, do not use Root user).
- Run docker.
- Upload your custom image to Dockerhub.

## Task 3
---------------

**(Docker Compose)**
- Create a Docker Compose setup for a Python server-client application where the client communicates with the server within a Docker network through different API/URI endpoints. 

- **Implement the Python server to handle:**

    - GET /health to return an OK status if the server is running.
    - POST /ping to return a JSON response {"type": "pong", "time": "current_time"}.
    - POST /data to accept a JSON request {"jsonrpc": "2.0", "method": "message-1"} and respond with the original message with the current time {"jsonrpc": "2.0", "method": "message-1", “time”:"current_time"}.

- **Implement the Python client to:**

    - Perform a health check by sending a GET request to /health.
    - Send a POST request to /ping with JSON {"type": "ping"} and handle the response.
    - Send a POST request {"jsonrpc": "2.0", "method": "message-1"} to /data and handle the response.
    - Repeat requests at 5 sec intervals in a while loop 
- Ensure the server is only accessible within the Docker network.
- Use Docker Compose depends_on and condition for services health checks.
