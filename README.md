# 📦 Inventory Management System

A secure and scalable **Inventory Management REST API** built with **FastAPI**. This project follows a clean layered architecture and provides authentication, user management, product management, and admin functionalities using **JWT Authentication**, **SQLAlchemy ORM**, **Alembic Migrations**, and **MySQL**.

---

## 🚀 Features

- 🔐 JWT Authentication & Authorization
- 👤 User Management
- 👑 Admin Management
- 📦 Product Management
- 🗄️ MySQL Database Integration
- ⚡ FastAPI REST API
- 🔄 Alembic Database Migrations
- 📖 Interactive Swagger Documentation
- 🏗️ Clean Layered Architecture
- 🔒 Environment Variable Configuration

---

## 🛠️ Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming Language |
| FastAPI    | Backend Framework    |
| SQLAlchemy | ORM                  |
| MySQL      | Database             |
| Alembic    | Database Migrations  |
| JWT        | Authentication       |
| Pydantic   | Data Validation      |
| Uvicorn    | ASGI Server          |

---

## 🏗️ Project Architecture

```text
Client
   │
   ▼
Routes
   │
   ▼
Controllers
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
MySQL Database
```

---

## 📁 Project Structure

```text
Inventory-Management-System/
│
├── app/
│   ├── config/
│   ├── controllers/
│   ├── middlewares/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── alembic/
├── migrations/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/inventory-management-system-fastapi.git
```

### 2. Navigate to the project directory

```bash
cd inventory-management-system-fastapi
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root using the provided `.env.example` file.

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=inventory_db
DB_USER=your_username
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## ▶️ Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI**

  ```
  http://127.0.0.1:8000/docs
  ```

- **ReDoc**

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 📌 API Modules

- Authentication
- User Management
- Product Management
- Admin Management

---

## 🔒 Security

- JWT Authentication
- Password Hashing
- Environment Variables (.env)
- SQLAlchemy ORM
- Layered Architecture

---

## 📈 Future Enhancements

- Role-Based Access Control (RBAC)
- Docker Support
- Unit & Integration Testing
- CI/CD Pipeline
- Inventory Analytics Dashboard
- Email Notifications

---

## 👨‍💻 Developed By

- **Laiba Irshad**
- **Shakir Hussain**

---

## 📄 License

This project is licensed under the **MIT License**.
