from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city", "chennai")
    api_key = "e084469d75cffef8d3cbccf824240565"  # 🔑 replace with your OpenWeather API key

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return f"<h3>Error: {response.get('message')}</h3>"

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
    <p><b>City:</b> {{weather['city']}}</p>
    <p><b>Temperature:</b> {{weather['temp']}} °C</p>
    <p><b>Description:</b> {{weather['description']}}</p>
    <img src="http://openweathermap.org/img/wn/{{weather['icon']}}.png">
    """
    return render_template_string(html, weather=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
