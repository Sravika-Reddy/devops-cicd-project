
# Automated CI/CD Pipeline for a Containerized Web Application

## 1. Project Overview

This project implements an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Flask-based web application using GitHub Actions and Docker.

Whenever a developer pushes code to the GitHub repository, GitHub Actions automatically executes test cases, builds a Docker image, and publishes the image to Docker Hub.

## 2. Project Objectives

- Automate application testing.
- Containerize the Flask application using Docker.
- Implement CI/CD using GitHub Actions.
- Automatically publish Docker images to Docker Hub.
- Deploy the containerized application locally.

## 3. Technologies Used

- Python – Application development
- Flask – Web framework
- Pytest – Automated testing
- Git and GitHub – Version control
- GitHub Actions – CI/CD automation
- Docker – Application containerization
- Docker Hub – Docker image registry

## 4. Project Architecture

Developer pushes code to GitHub
        |
        v
GitHub Actions Pipeline
        |
        v
Install Dependencies
        |
        v
Run Automated Tests
        |
        v
Build Docker Image
        |
        v
Push Image to Docker Hub
        |
        v
Pull and Run Docker Container

## 5. CI/CD Pipeline Workflow

1. Developer pushes application code to GitHub.
2. GitHub Actions automatically triggers the workflow.
3. Python environment and dependencies are configured.
4. Pytest executes automated test cases.
5. Docker builds an image if testing succeeds.
6. GitHub Actions authenticates with Docker Hub using GitHub Secrets.
7. The Docker image is published to Docker Hub.

## 6. Automated Testing

The project includes two test cases:

- Home page test: verifies that the application returns HTTP 200 and the expected welcome message.
- Invalid route test: verifies that an unknown URL returns HTTP 404.

Both test cases passed during local verification.

## 7. Docker Deployment

The Flask application is packaged into a Docker image.

The published image can be downloaded using:

```bash
docker pull YOUR_DOCKERHUB_USERNAME/devops-cicd-app:latest
```

Run the application using:

```bash
docker run -d -p 5000:5000 YOUR_DOCKERHUB_USERNAME/devops-cicd-app:latest
```

Access the application at:

http://127.0.0.1:5000/

## 8. Results

- Flask application successfully developed.
- Automated test cases executed successfully.
- Docker image built successfully.
- GitHub Actions CI/CD workflow executed successfully.
- Docker image published to Docker Hub.
- Containerized application deployed and verified locally.

## 9. Conclusion

This project demonstrates how CI/CD automation simplifies software delivery by combining automated testing, Docker containerization, image publishing, and application deployment. It reduces manual effort and provides a repeatable workflow for delivering application updates.
