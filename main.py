import requests
import json
from flask import Flask


def get_currencies_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    currencies = list(data['Valute'].values())
    return currencies


app = Flask(__name__)


def create_html(currencies):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in currencies[0]:
        text += f'<th><th>'
    text += '</tr>'
    for curr in currencies:
        text += '<tr>'
        for v in curr.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    currencies = get_currencies_list()
    html = create_html(currencies)
    return html


if __name__ == "__main__":
    app.run()
