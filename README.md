
# 🐳 Flask Feedback Web App

A lightweight **Flask-based feedback application** containerized using **Docker** and served with **Gunicorn**.  
Includes a `/health` endpoint for automatic container health monitoring and supports persistent storage for user feedback.

---

## 🚀 Run Locally (without Docker)

```bash
# Clone this repository
git clone https://github.com/AshwinSajii/flask-feedback-app.git
cd flask-feedback-app

# (Optional) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
````

Then visit → [http://localhost:5000](http://localhost:5000)

---

## 🐳 Run with Docker

```bash
# Pull from Docker Hub
docker pull ashwinsajii/flask-feedback-app:latest

# Run the container
docker run -d -p 5000:5000 ashwinsajii/flask-feedback-app
```

---

## 📦 Example with Persistent Volume

```bash
docker run -d \
  --name flask-feedback-app \
  -p 5000:5000 \
  -v "$(pwd)/feedback.txt":/home/appuser/app/feedback.txt \
  ashwinsajii/flask-feedback-app
```

This ensures feedback data is saved on your host even after container restarts.

---

## 🧠 Features

* 🧩 **Flask Web App** – simple feedback form built with HTML & Python
* ⚙️ **Gunicorn** – production-grade WSGI server
* ❤️ **Health Check** – `/health` endpoint for container monitoring
* 💾 **Persistent Volume** – save feedback data outside container
* ☁️ **Portable** – runs identically on any environment (Linux, Windows, Cloud)

---

## 🧱 Tech Stack

| Tool                   | Purpose                 |
| ---------------------- | ----------------------- |
| **Python 3.12 (Slim)** | Base environment        |
| **Flask**              | Backend framework       |
| **Gunicorn**           | WSGI production server  |
| **Docker**             | Containerization        |
| **Ubuntu (WSL2)**      | Development environment |

---

## 🩺 Health Check

Docker automatically verifies the container health every 30 seconds using:

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD curl -f http://127.0.0.1:5000/health || exit 1
```

You can manually check health status:

```bash
docker inspect --format='{{.State.Health.Status}}' flask-feedback-app
```

---

## 🧰 Project Structure

```
flask-feedback-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── feedback.html
│   ├── thank_you.html
│   └── view.html
│
└── README.md
```

---

## 🧾 Docker Hub Image

📦 Available publicly on Docker Hub:
👉 [https://hub.docker.com/r/ashwinsajii/flask-feedback-app](https://hub.docker.com/r/ashwinsajii/flask-feedback-app)

Pull the image:

```bash
docker pull ashwinsajii/flask-feedback-app:latest
```

---

## 👤 Author

**Ashwin Saji**
💻 System Administrator | Aspiring Cloud & DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-ashwinsajii-181717?style=for-the-badge\&logo=github)](https://github.com/AshwinSajii)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ashwin%20Saji-0A66C2?style=for-the-badge\&logo=linkedin)](https://www.linkedin.com/in/ashwinsajii)

---

⭐ **If you liked this project, consider giving it a star!**

