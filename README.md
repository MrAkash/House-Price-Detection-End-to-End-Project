# 🏠 End-to-End House Price Prediction System

A full-stack Machine Learning web application that predicts house prices using a trained ML model.  

This project demonstrates the complete ML deployment workflow including:
- Machine Learning model training
- FastAPI backend development
- Streamlit frontend development
- Docker containerization
- Cloud deployment using Render

---

# 🚀 Live Demo

## 🌐 Frontend
https://your-frontend-url.onrender.com

## ⚡ Backend API Docs
https://your-backend-url.onrender.com/docs

---

# 🧠 Project Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Machine Learning Model
  ↓
Prediction Response
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| Scikit-learn | Machine Learning |
| Docker | Containerization |
| Docker Compose | Multi-container setup |
| Render | Cloud Deployment |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
project/
│
├── backend/
│   ├── main.py
│   ├── model.pkl
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── train_model.py
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Features

✅ House price prediction  
✅ FastAPI REST API  
✅ Interactive Streamlit frontend  
✅ Dockerized application  
✅ Multi-container architecture  
✅ Cloud deployment on Render  
✅ Frontend-backend integration  

---

# 🧠 Machine Learning Model

The model predicts house prices based on:
- Area
- Number of Bedrooms
- Age of House

### Algorithm Used
- Linear Regression

---

# 🚀 Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/end-to-end-house-price-prediction.git
```

---

## 2️⃣ Move Into Project Directory

```bash
cd end-to-end-house-price-prediction
```

---

## 3️⃣ Run Application Using Docker Compose

```bash
docker compose up --build
```

---

# 🌍 Access Application

## Frontend

```text
http://localhost:8501
```

## Backend API Documentation

```text
http://localhost:8000/docs
```

---

# 🔥 API Endpoint

## Predict House Price

### Endpoint

```http
POST /predict
```

### Request Body

```json
{
  "area": 1500,
  "bedrooms": 3,
  "age": 5
}
```

### Response

```json
{
  "predicted_price": 300000
}
```

---

# 🐳 Docker Support

This project is fully containerized using Docker and Docker Compose.

### Services
- Frontend Container
- Backend Container

---

# ☁️ Cloud Deployment

The application is deployed on Render.

### Deployment Includes
- Backend deployment
- Frontend deployment
- Automatic GitHub redeployment

---

# 📚 Learning Outcomes

This project helped in understanding:

- Machine Learning deployment
- REST API development
- Frontend-backend communication
- Docker containerization
- Docker Compose
- Cloud deployment
- Production-level project structure

---

# 👨‍💻 Author

Akash Kadam

---

# ⭐ Future Improvements

- Add database integration
- Add authentication system
- Improve UI/UX
- Add advanced ML model
- Add prediction history
- Kubernetes deployment

---

# 📜 License

This project is created for learning and educational purposes.
