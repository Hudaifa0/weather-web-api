from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")

API_KEY = "c8cb3b93e5d3ed1c629e924cfd2ab655"  # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, city: str = None):
    result = None
    error = None

    if city:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            result = {
                "city": city.title(),
                "weather": data["weather"][0]["description"].capitalize(),
                "temperature": data["main"]["temp"],
                "wind": data["wind"]["speed"],
                "humidity": data["main"]["humidity"]
            }
        else:
            error = data.get("message", "Invalid city name or error occurred.")

    return templates.TemplateResponse("form.html", {"request": request, "result": result, "error": error})
