<p align="center">
  <img src="https://img.shields.io/badge/Backend-Django%205.2-092E20?style=flat&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-003B57?style=flat&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/API%20Docs-Swagger-85EA2D?style=flat&logo=swagger&logoColor=black" />
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=flat&logo=docker&logoColor=white" />
</p>

<h1 align="center">👤 Personnel Management API</h1>

<p align="center"><strong>A professional, production-ready REST API for modern personnel and department tracking systems 🚀</strong></p>


<div align="center">
  <h3>
    <a href="https://umit8100.pythonanywhere.com/swagger/">
      🖥️ Live Demo (Swagger)
    </a>
     | 
    <a href="https://github.com/umitarat-dev/personnel-management-api">
      📂 Repository
    </a>
  </h3>
</div>

<p align="center">
  <a href="https://umit8100.pythonanywhere.com/swagger/">
    <img src="./assets/personnel-api.gif" alt="Interactive Swagger Documentation" width="700"/>
  </a>
</p>

## 📚 Navigation
- [🚀 Live API Documentation](#-live-api-documentation)
- [📦 Key Features](#-key-features)
- [🛠️ Built With](#️-built-with)
- [⚙️ Setup & Installation](#️-setup--installation)
- [📬 Contact Information](#-contact-information)


## 🚀 Live API Documentation
The API is fully documented and interactive. Note: Swagger and Redoc are accessible without login for demonstration purposes.
* **Swagger UI:** [https://umit8100.pythonanywhere.com/swagger/](https://umit8100.pythonanywhere.com/swagger/)
* **ReDoc:** [https://umit8100.pythonanywhere.com/redoc/](https://umit8100.pythonanywhere.com/redoc/)]

> **Note:** In production mode (`ENV_NAME=prod`), Swagger documentation is automatically hidden for security best practices.


## 📦 Key Features
* **Department & Personnel Tracking:** Full CRUD operations for managing organizational structures.
* **Role-Based Authorization:** Granular access control for Superusers, Staff, and Regular Users.
* **Dockerized Infrastructure:** Containerized environment with PostgreSQL for seamless local and production orchestration.
* **Environment-Aware Config:** Hybrid setup supporting SQLite (Dev) and PostgreSQL (Prod) via environment variables.
* **Professional Logging:** Integrated system logs for tracking API activities and debugging.


## 🛠️ Built With
* **Core:** [Django 5.2](https://www.djangoproject.com/) & [Django REST Framework](https://www.django-rest-framework.org/)
* **Auth:** [dj-rest-auth](https://dj-rest-auth.readthedocs.io/) with Token Authentication
* **Database:** PostgreSQL (Production) & SQLite (Local Testing)
* **API Documentation:** [drf-yasg (Swagger/Redoc)](https://drf-yasg.readthedocs.io/)


## ⚙️ Setup & Installation

### Option 1: Docker (Recommended)
The fastest way to get the system running with PostgreSQL:
```bash
git clone [https://github.com/umitarat-dev/personnel-management-api.git](https://github.com/umitarat-dev/personnel-management-api.git)
cd personnel-management-api
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```


### Option 2: Local Development

#### 1. Clone & Environment:

```bash
git clone [https://github.com/umitarat-dev/personnel-management-api.git](https://github.com/umitarat-dev/personnel-management-api.git)
python -m venv env
source env/bin/activate  # macOS/Linux
# env\Scripts\activate  # Windows
```

#### 2. Configuration:

Create a .env file in the root:
```bash
SECRET_KEY=your_secret_key
ENV_NAME=dev
DEBUG=True
DJANGO_LOG_LEVEL=WARNING
```

#### 3. Install & Run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## 📬 Contact Information

I am always open to discussing new projects, creative ideas, or opportunities to be part of your visions.

* **LinkedIn:** [linkedin.com/in/umit-arat](https://www.linkedin.com/in/umit-arat/)
* **Email:** [umitarat8098@gmail.com](mailto:umitarat8098@gmail.com)
* **GitHub:** [github.com/umitarat-dev](https://github.com/umitarat-dev) (Current Workspace)