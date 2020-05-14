from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Toronto Weather API. Go to /weather to get the weather :)"


@app.route("/weather", methods=["GET"])
def weather():
    from bs4 import BeautifulSoup
    import requests

    url = "https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")
    span_list = []

    for weather in soup.find_all("span", class_=""):
        span_list.append(weather.text)

    weather = span_list[27]

    feel = soup.find("span", class_="deg-feels")
    return feel.text


if __name__ == "__main__":
    app.run()
