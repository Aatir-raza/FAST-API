# FastAPI – Data Validation & Patient Management

A Python-based backend project built with **FastAPI**, focusing on data validation, model validation, schema management, and patient data handling.

## 🚀 Features

- **FastAPI Integration** – Backend API development using FastAPI.
- **Field Validation** – Validate individual fields using custom validation logic.
- **Model Validation** – Validate complete data models.
- **Schema Management** – Define and manage structured data schemas.
- **Typing Utilities** – Reusable typing and utility functions.
- **Patient Management** – Handle patient-related data.
- **JSON Data Handling** – Store and manage patient records using JSON.

## 📁 Project Structure

```text
FASTAPI/
│
│
├── .gitignore
├── main.py
├── field_validator.py
├── model_validator.py
├── schemas.py
├── typing_utils.py
├── patients.py
└── patients.json
```

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- JSON

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone <repository-url>
```

**2. Navigate to the project directory**

```bash
cd FASTAPI
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install fastapi uvicorn pydantic
```

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

## 📖 API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🎯 Project Objective

The objective of this project is to understand and implement backend development concepts using FastAPI, Python type hints, data validation, and structured data management.

## 👨‍💻 Author

Developed as part of learning and practicing Python backend development with FastAPI.
