# PST
## Password Strength Tester (PST)

Welcome to the Password Strength Tester (PST) project repository! PST is a tool to evaluate the strength of passwords.

## Overview

This project provides a Dockerized setup for running the Password Strength Tester application using Streamlit. Due to the limitation of uploading larger files to GitHub, we have containerized the necessary files and dependencies to ensure easy access and execution of the project. To utilize this project, you'll need to pull the Docker image from a Docker registry.

## Prerequisites

Before getting started, ensure that you have Docker installed on your system. You can download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).

## Usage

To run the Password Strength Tester application locally using Docker, follow these steps:

1. Pull the Docker image from the Docker registry:
    ```bash
    docker pull atom1326/pst:latest
    ```

2. Once the image is pulled successfully, you can run the Docker container with the following command:
    ```bash
    docker run -d -p 8501:8501 atom1326/pst:latest
    ```

3. After the container is up and running, you can access the Password Strength Tester application in your web browser at:
    ```
    http://localhost:8501
    ```

**Note:**
Due to the inability to upload larger files, we have containerized the necessary files and dependencies. If you have any questions or encounter any issues while running the project, feel free to open an issue in this repository.

Enjoy testing your passwords with PST!

If you want to contribute you can check out the repository files:
```bash
git clone https://github.com/RushiChaganti/PST.git
```

[![Watch the video][https://github.com/RushiChaganti/Dockerized_PST/blob/main/password_capture.mp4]]

Feel free to let me know if you need any further modifications or additions!
