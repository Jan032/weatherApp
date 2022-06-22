import requests

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    city = request.form.get("city")
    apiKey = "e9ad246b97789f4ca066a203c03daf0a"
    units = "metric"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units={units}"

    data = requests.get(url=url)

    return render_template("indexx.html", data=data.json())


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)