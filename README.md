# 📌 Flask Feedback App — DevOps Portfolio Project

A simple Flask-based web application containerized with Docker and prepared for real-world DevOps workflows.  
This project demonstrates **Linux fundamentals, containerization, Docker Hub usage, health checks, Git CLI workflow**, and serves as the foundation for future enhancements like CI/CD, Terraform deployment, Kubernetes, and monitoring.

---

## 🚀 Live Demo (Coming Soon)
➡️ *Once deployed on AWS EC2 or Kubernetes, add the public URL here.*

---

# 🧠 Project Overview

This is a beginner-friendly Flask feedback application built to showcase DevOps skills rather than full-stack development.

The project demonstrates:

- Building and running a Flask app  
- Dockerizing the app using a custom Dockerfile  
- Publishing images to Docker Hub using CLI  
- Health checks for container reliability  
- Git/GitHub workflow entirely via command line  
- Production-ready structure  
- Future-ready for CI/CD, Terraform, and Kubernetes  

This app will evolve into a **complete DevOps pipeline project**, starting from a simple Python app to a fully automated and cloud-deployed service.

---

# 🧰 Tech Stack

### Backend
- Python Flask  
- HTML + Jinja templates  

### DevOps / Infra
- Docker  
- Docker Hub  
- Linux (Ubuntu)  
- Git CLI  
- Health checks  
- (Upcoming) GitHub Actions, Terraform, AWS EC2, Nginx, Kubernetes  

---

# 🗂️ Project Structure

```

flask-feedback-app/
├── app.py
├── templates/
│   ├── index.html
│   └── feedback.html
├── static/
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md

````

---

# 🧪 Features Implemented

### ✔ Simple Flask Web App  
Basic form-based feedback application.

### ✔ Dockerized Application  
- Custom Dockerfile  
- Lightweight Python image  
- Ready for production improvements  

### ✔ Docker Hub Integration  
Image pushed using **only Linux commands**, no manual UI upload.

### ✔ Health Check Endpoint  
`/health` returns:

```json
{ "status": "ok" }
````

Useful for Docker, Kubernetes, ECS, uptime checks, etc.

### ✔ GitHub Managed via Terminal

Repo initialized, committed, and pushed using Git CLI only.

---

# 🐳 Docker Usage

### Build the image

```bash
docker build -t your-dockerhub-username/flask-feedback-app .
```

### Run the container

```bash
docker run -d -p 5000:5000 your-dockerhub-username/flask-feedback-app
```

### Push to Docker Hub

```bash
docker login
docker tag flask-feedback-app your-dockerhub-username/flask-feedback-app:latest
docker push your-dockerhub-username/flask-feedback-app:latest
```

---

# 🧪 Health Check

Check container health:

```bash
curl http://127.0.0.1:5000/health
```

Output:

```json
{ "status": "ok" }
```

---

# 📸 Screenshots

> Add later:
>
> * UI screenshot
> * Terminal screenshot of Docker push
> * Architecture diagram

Place all images under `/assets/`.

---

# 🛠️ Planned Improvements (DevOps Roadmap)

## Phase 1 — Complete (✓)

* Flask app
* Dockerfile
* Docker Hub push
* Repo via Git CLI
* Health endpoint

## Phase 2 — In Progress (⏳)

* Improve Dockerfile
* Add pytest test
* Add docker-compose
* Add screenshots & README polish

## Phase 3 — Upcoming (🔥 DevOps Work)

### 1️⃣ CI/CD Pipeline — GitHub Actions

* Build image
* Run tests
* Push to Docker Hub
* Auto-deploy to server

### 2️⃣ Deploy to AWS EC2

* Run Docker container on EC2
* Optionally add Nginx reverse proxy

### 3️⃣ Infrastructure as Code — Terraform

* Provision EC2
* Add security groups
* Auto-deploy container using user data

### 4️⃣ Kubernetes Deployment

* Deployment + Service
* Liveness/readiness probes
* Optional Ingress / EKS

### 5️⃣ Monitoring

* Logging improvements
* Prometheus metrics
* Grafana dashboards

---

# 📡 Run Locally (No Docker)

```bash
pip install -r requirements.txt
python app.py
```

App runs at:

```
http://127.0.0.1:5000
```

---

# 🧑‍💻 What I Learned

* Flask basics
* Dockerfile creation
* Working with Docker Hub
* Git CLI workflow
* Creating a health check endpoint
* Planning a full DevOps lifecycle
* Understanding how to evolve a simple web app into a production-ready deployment

---

# 🔗 Links

### GitHub Repo

➡️ [https://github.com/AshwinSajii/flask-feedback-app](https://github.com/AshwinSajii/flask-feedback-app)

### Docker Hub

➡️ *[Add your Docker Hub repo link here](https://hub.docker.com/repository/docker/ashwinsajii/flask-feedback-app/general)*

### LinkedIn

➡️ [https://www.linkedin.com/in/ashwinsajii/](https://www.linkedin.com/in/ashwinsajii/)

---

# 🙌 Next Steps

I will continue improving this project by adding:

* CI/CD
* Cloud deployment
* Terraform
* Kubernetes
* Nginx reverse proxy
* Monitoring & observability
* Security best practices

Stay tuned for updates!

```
