#instalar dependencias 
pip install -r requirements.txt

#-- Correr Proyecto --
uvicorn app.main:app --reload

#----  BD  ----

CREATE DATABASE login_api;

USE login_api;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
