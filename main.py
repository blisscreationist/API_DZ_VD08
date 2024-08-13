from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quote = None

    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()

    # Получение случайной цитаты
    quote = get_random_quote()

    return render_template("index.html", weather=weather, news=news, quote=quote)


def get_weather(city):
    api_key = "039762cd926c00cbb8bf9ae0a4431af1"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


def get_news():
    api_key = "c2d88b70c2734e7ca28ae7bf4da6e9fa"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])


def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


if __name__ == '__main__':
    app.run(debug=True)