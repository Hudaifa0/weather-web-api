# 🌦️ Weather Checker

A modern and responsive web application built with **FastAPI** and **Jinja2** that fetches real-time weather data using the **OpenWeatherMap API**. Designed with a clean and mobile-friendly UI and deployed on **Vercel**.

## 🔗 Live Demo
Check it out live here: [Weather Checker App](https://weather-web-api-git-main-christophers-projects-9ac7965f.vercel.app/)

## ✨ Features

- 🔍 Search weather by city
- 📡 Real-time data from OpenWeatherMap
- 💻 Clean and responsive UI
- ☁️ FastAPI backend with HTML templating (Jinja2)
- 🚀 Deployed on Vercel

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2
- requests

### Installation

1. Clone the repository:
    ```bash
        git clone https://github.com/Gggghgggh/weather-web-api.git
        cd weather-checker
    
2. Install dependencies:

       pip install -r requirements.txt

4. Create a .env file or replace the API_KEY in index.py with your OpenWeatherMap API key.
   
6. Run locally:
   
       uvicorn api.index:app --reload

8. Visit http://localhost:8000 to view the app.
   
## 📦 Directory Structure

        weather-web-api/
        │
        ├── api/
        │   ├── index.py
        │   ├── templates/
        │   │   └── form.html
        │   └── static/ (optional, for icons)
        ├── vercel.json
        ├── README.md
        └── requirements.txt


