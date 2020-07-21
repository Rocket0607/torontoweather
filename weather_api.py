from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Toronto Weather API :)"


@app.route("/weather")
def weather():
    from bs4 import BeautifulSoup
    import requests

    url = "https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    temp = soup.find(
        "span", class_="_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt")
    return temp.text


@app.route("/feel")
def feel():
    from bs4 import BeautifulSoup
    import requests

    url = "https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    feel = soup.find(
        "span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
    return feel.text


@app.route("/moon")
def moon():
    from bs4 import BeautifulSoup
    import requests

    url = "https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    moons = soup.find_all(
        "div", class_="_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q")

    return str(moons[7].text)


@app.route("/wind")
def wind():
    from bs4 import BeautifulSoup
    import requests

    url = "https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    wind = soup.find(
        "span", class_="_-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c undefined")

    return wind.text


@app.route("/humidity")
def humidity():
    from bs4 import BeautifulSoup
    import requests

    url = "https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    humidity = soup.find_all(
        "div", class_="_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q")

    return str(humidity[2].text)


if __name__ == "__main__":
    app.run()
