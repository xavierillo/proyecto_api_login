# como instalar dependencias 
pip install -r requirements.txt

# ejecutar proyecto local sin docker
uvicorn app.main:app --reload

# Base de datos

CREATE DATABASE login_api;

USE login_api;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


# registro
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"javier\", \"email\": \"javier@example.com\", \"password\": \"123456\"}"


# login 

curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"javier\", \"password\": \"123456\"}"


# Docker 
sudo docker build -t proyecto_api .
sudo docker stop api && sudo docker rm api
sudo docker run -d --network host --name api proyecto_api
