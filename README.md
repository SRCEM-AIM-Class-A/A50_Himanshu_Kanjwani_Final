# Web Applications with Flask, Django, and Docker Compose

## 📌 Overview

This project demonstrates the development and containerization of two web applications — one built using **Flask** and the other using **Django** — both managed using **Docker Compose**.

```markdown
## 🧩 Project Structure
SL-3/
├── flask-app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── django-app/
│   ├── manage.py
│   ├── myproject/
│   ├── items/
│   ├── Dockerfile
│   ├── requirements.txt
├── docker-compose.yml
```

---

## 🚀 Part 1: Flask App

### Features

- Homepage displays **"Hello, World!"**
- `/greet` route displays a **form** to collect user's name and age.
- Displays a personalized greeting message.
- Includes **basic error handling** for invalid inputs.
- Styled using **inline CSS**.

### Run locally

```bash
cd flask-app
python app.py
```

### Docker

```bash
docker build -t flask-final .
docker run -p 5000:5000 flask-final
```

---

## 🧱 Part 2: Django App

### Features

- Displays a list of items (e.g., books/products) on the homepage.
- **Admin panel** for adding and modifying items.
- Homepage form to add new items.

### Run locally

```bash
cd django-app
python manage.py runserver
```

### Docker

```bash
docker build -t django-final .
docker run -p 8000:8000 django-final
```

---

## 🐳 Part 3: Docker Compose

Runs both Flask and Django apps in separate containers.

```bash
docker-compose up --build
```

- Flask app: [http://localhost:5000](http://localhost:5000)
- Django app: [http://localhost:8000](http://localhost:8000)

---

## 📝 Submission

- 🔗 GitHub Repository: *https://github.com/SRCEM-AIM-Class-A/A50_Himanshu_Kanjwani_Final.git*
- 🐋 Docker Hub Repositories:
  - Flask App: *https://hub.docker.com/repository/docker/himanshuk713/flask-final*
  - Django App: *https://hub.docker.com/repository/docker/himanshuk713/django-final*

---

## 🙋‍♂️ Author

**Himanshu Kanjwani**  
**Student, RBU Nagpur**
