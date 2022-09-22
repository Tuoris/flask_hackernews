import requests
from flask import Flask, render_template

from constants import (
    ITEMS_API_URL,
    NEWS_API_URL,
)

app = Flask(__name__)


@app.template_filter("pluralize")
def pluralize(number, singular="", plural="s"):
    if number == 1:
        return singular
    else:
        return plural


@app.route("/")
def home_view():
    news_response = requests.get(NEWS_API_URL)
    news = news_response.json()

    return render_template("news.html", news=news)


@app.route("/<item_id>")
def item_view(item_id):
    item_response = requests.get(f"{ITEMS_API_URL}/{item_id}")
    item = item_response.json()

    return render_template("item.html", item=item)
