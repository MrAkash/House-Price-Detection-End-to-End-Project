🏠 House Price Prediction System
A full-stack Machine Learning web application for predicting house prices using a trained ML model.

This project demonstrates:
Machine Learning model deployment
Backend API development
Frontend integration
Docker containerization
Cloud deployment

🚀 Live Demo

https://your-frontend-url.onrender.com

🧠 Project Architecture

User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Machine Learning Model
  ↓
Prediction Response

🛠️ Technologies Used
Technology
Purpose
Python
Core programming language
FastAPI
Backend API
Streamlit
Frontend UI
Scikit-learn
ML model training
Docker
Containerization
Docker Compose
Multi-container setup
Render
Cloud deployment
GitHub
Version control

📂 Project Structure

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

⚙️ Features
✅ House price prediction
✅ FastAPI backend API
✅ Streamlit frontend UI
✅ Dockerized application
✅ Multi-container architecture
✅ Cloud deployment
✅ REST API integration

🧠 Machine Learning Model
The model is trained using:
Area
Number of Bedrooms
Age of House

Algorithm used:
Linear Regression

🚀 Local Setup
1️⃣ Clone Repository
git clone <your-github-repo-url>

2️⃣ Move Into Project
cd project-name

3️⃣ Run With Docker Compose
docker compose up --build

🌍 Access Application
Frontend
http://localhost:8501
Backend API Docs
http://localhost:8000/docs

🔥 API Endpoint
Predict House Price
Endpoint

POST /predict
Request Body
J
{
  "area": 1500,
  "bedrooms": 3,
  "age": 5
}
Response

{
  "predicted_price": 300000
}

🐳 Docker Deployment
This project uses:
Docker
Docker Compose
to containerize:
frontend
backend
ML model environment

☁️ Cloud Deployment
The project is deployed using:
Render

Deployment includes:
Backend deployment
Frontend deployment
Automatic GitHub redeployment

📚 Learning Outcomes
This project helped in understanding:
✅ Machine Learning deployment
✅ REST APIs
✅ Frontend-backend communication
✅ Docker containerization
✅ Cloud deployment
✅ Production architecture

👨‍💻 Author
Akash Kadam

⭐ Future Improvements
Add database integration
Add authentication
Improve UI design
Add advanced ML model
Add user history
Deploy with Kubernetes

📜 License
This project is for learning and educational purposes
