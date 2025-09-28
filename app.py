from flask import Flask, request, render_template_string
from pyngrok import ngrok
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city", "chennai")
    api_key = "YOUR_API_KEY"  # replace with your real OpenWeather key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    weather_data = {
        "city": response["name"],
        "temp": response["main"]["temp"],
        "description": response["weather"][0]["description"],
        "icon": response["weather"][0]["icon"]
    }
    html = """
    <h2>🌤️ Weather App</h2>
    <form method="get">
        <input type="text" name="city" placeholder="Enter city name">
        <input type="submit" value="Get Weather">
    </form>
    <p>City: {{weather['city']}}</p>
    <p>Temperature: {{weather['temp']}} °C</p>
    <p>Description: {{weather['description']}}</p>
    <img src="http://openweathermap.org/img/wn/{{weather['icon']}}.png">
    """
    return render_template_string(html, weather=weather_data)

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print("Public URL:", public_url)
    app.run(port=5000)
