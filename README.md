# DevOps Portfolio Project

This project demonstrates a simple CI/CD pipeline using GitLab, Docker, and Kubernetes. The application is a basic Flask web app with a simple REST API that will be containerized using Docker and deployed to a Kubernetes cluster.

## Prerequisites

- GitLab account
- Docker installed on your local machine
- A Kubernetes cluster (e.g., Minikube, GKE, EKS)
- `kubectl` configured to access your Kubernetes cluster

## Project Structure

```
devops-portfolio-project/
├── app/
│   ├── app.py
│   ├── requirements.txt
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
├── .gitlab-ci.yml
├── Dockerfile
└── README.md
```

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://gitlab.com/AmirBargaoui/FlaskDeployPipeline.git
cd devops-portfolio-project
```

### 2. Build and Run the Application Locally

Build the Docker image for the Flask application:

```sh
docker build -t flask-app .
```

Run the Docker container locally to ensure the application works as expected:

```sh
docker run -p 5000:5000 flask-app
```

Open your browser and navigate to `http://localhost:5000` to see the application running. You should see "Hello, World!" and be able to access the API endpoint at `http://localhost:5000/api/data`.

### 3. Push the Docker Image to a Registry

Tag the Docker image with your Docker Hub username and push it to Docker Hub:

```sh
docker tag flask-app amirbargaoui/flask-app:latest
docker push amirbargaoui/flask-app:latest
```

### 4. Deploy to Kubernetes

Ensure your `kubectl` is configured to interact with your Kubernetes cluster. Apply the Kubernetes manifests to deploy the application:

```sh
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### 5. Set Up GitLab CI/CD

1. Create a new project in GitLab and push your repository.
2. In your GitLab project, go to **Settings > CI / CD > Variables** and add the following variables:
   - `CI_REGISTRY_IMAGE`: Your Docker registry image name (e.g., `registry.gitlab.com/amirbargaoui/FlaskDeployPipeline`)

### 6. Trigger the Pipeline

Push changes to your GitLab repository to trigger the CI/CD pipeline:

```sh
git add .
git commit -m "Initial commit"
git push origin main
```

The pipeline will build the Docker image, push it to the registry, and deploy the application to your Kubernetes cluster.

### 7. Verify the Deployment

After the deployment is complete, you can verify that the application is running correctly on your Kubernetes cluster. Use the following command to get the external IP address of the service:

```sh
kubectl get svc flask-app-service
```

Open your browser and navigate to the external IP address to see the application running. You should see "Hello, World!" and be able to access the API endpoint at `/api/data`.

### Conclusion

This project provides a basic example of using GitLab CI/CD, Docker, and Kubernetes to deploy a web application. You can extend this project by adding more complex features, monitoring, logging, and security practices.