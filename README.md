# Employee Management System

A Django-based system for managing employee data with REST APIs, authentication, filtering, and visualization capabilities.

## 🚀 Features

- **CRUD APIs** for Employees, Departments, Attendance, and Performance
- **Token Authentication** to secure API access
- **Swagger UI** for interactive API documentation
- **Data Seeding** using Faker for quick testing
- **Filtering & Search** in API endpoints
- **Visualization**:  
  - Pie Chart: Employees per Department  
  - Bar Chart: Monthly Attendance Overview (with Present/Absent/Late breakdown)
- Works with SQLite (default) or PostgreSQL
- Ready to deploy with **Docker**

## 🧩 Technologies Used

- Python 3.12+
- Django 4.x / Django REST Framework (DRF)
- drf-yasg (Swagger Documentation)
- python-dotenv, Faker, django-filter
- Chart.js for visualizations
- Docker for containerization

## 📦 Prerequisites

- Python 3.10+
- Docker (optional)

## 🛠️ Setup Instructions
- Create and activate virtual environment:
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

- Install dependencies:
pip install -r requirements.txt

- Apply migrations:
python manage.py migrate

- Seed database with fake data:
python manage.py seed_db

- Create a superuser
python manage.py createsuperuser

- Run development server:
python manage.py runserver

Visit http://localhost:8000/swagger/ to view the API docs
Visit http://localhost:8000/dashboard/ to see visualizations


- Example API Requests
Get All Employees : GET /api/employees/
Filter by Department : GET /api/employees/?department=1
Search by Name or Email : GET /api/employees/?search=john
Login to Get Token : POST /api/login/
Get Monthly Attendance : GET /api/monthly-attendance/

### Option A: Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/employee-management-system.git 
   cd employee-management-system