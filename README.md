# 📌 Flask Feedback App — DevOps Mini Project

A **small, focused Flask application** used to demonstrate **core DevOps fundamentals** without overengineering. The project intentionally keeps the application scope simple while applying **production-minded practices** like containerization, testing, and CI automation.

> **Scope note:** This is a *mini project*. The goal is correctness, clarity, and real-world workflows — not scale or complex infrastructure.

---

## 🚀 Live Demo

➡️ *Optional*: Add a public URL if/when you deploy the Docker image to a cloud VM or PaaS.

---

## 🧠 Project Overview

This project is a basic feedback web app built with Flask. The application itself is intentionally simple so that the focus stays on **DevOps practices**:

* Containerization with Docker
* Reliable application startup using Gunicorn
* Health checks for service monitoring
* Automated testing
* Continuous Integration with GitHub Actions
* Clean Git workflow using the CLI

The result is a **production-ready mini application**, suitable for learning, demos, and interviews.

---

## 🧰 Tech Stack

### Backend

* Python 3.12
* Flask
* Jinja2 templates
* SQLite (local, file-based)

### DevOps / Tooling

* Docker
* Gunicorn (WSGI server)
* Git & GitHub (CLI workflow)
* GitHub Actions (CI)
* Linux (Ubuntu / WSL)

---

## 🗂️ Project Structure

```
flask-feedback-app/
├── app.py
├── models.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── feedback.html
│   ├── thank_you.html
│   └── view.html
├── static/
│   └── style.css
├── tests/
│   ├── conftest.py
│   └── test_health.py
├── instance/
│   └── app.db
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│   └── ci.yml
└── README.md
```

---

## ✨ Features

### ✔ Flask Web Application

* Simple feedback submission flow
* Login & registration
* Role-based access (admin vs user)

### ✔ Health Check Endpoint

```http
GET /health
```

Response:

```json
{ "status": "ok" }
```

Useful for:

* Docker health checks
* CI validation
* Monitoring and uptime probes

---

## 🐳 Docker

The application is fully containerized and runs with **Gunicorn**.

### Build image

```bash
docker build -t flask-feedback .
```

### Run container

```bash
docker run -p 5000:5000 flask-feedback
```

App available at:

```
http://localhost:5000
```

---

## 🧪 Testing

Basic automated tests are included to validate service health.

### Run tests locally

```bash
pytest
```

---

## 🔄 CI Pipeline (GitHub Actions)

A minimal **Continuous Integration pipeline** runs on every push to `main`.

The pipeline:

1. Installs dependencies
2. Runs automated tests
3. Builds the Docker image

This ensures the application:

* Boots correctly
* Passes tests
* Remains Docker-compatible

---

## 📦 Why This Is a Mini Project

This project deliberately avoids unnecessary complexity:

❌ No Kubernetes
❌ No Terraform
❌ No cloud provisioning
❌ No microservices

Instead, it demonstrates:

✅ Correct Docker usage
✅ CI fundamentals
✅ Debugging real container issues
✅ Production-aware Flask setup

This balance makes it ideal as a **portfolio-ready mini project**.

---

## 🧠 What I Learned

* Writing Dockerfiles for Python web apps
* Running Flask with Gunicorn in containers
* Debugging SQLite + Docker filesystem issues
* Writing CI-safe tests
* Configuring GitHub Actions pipelines
* Using Git entirely via CLI
* Knowing when *not* to add more infrastructure

---

## 🔗 Links

* **GitHub**: [https://github.com/AshwinSajii/flask-feedback-app](https://github.com/AshwinSajii/flask-feedback-app)
* **LinkedIn**: [https://www.linkedin.com/in/ashwinsajii/](https://www.linkedin.com/in/ashwinsajii/)

---

## ✅ Project Status

**Complete.**

This project is intentionally finished at this stage. Any future work (cloud deployment, IaC, Kubernetes) will be done in **separate, dedicated projects**.

---

> *Simple app. Correct engineering. Clean DevOps workflow.*
