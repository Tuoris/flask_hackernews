from urllib.parse import urlparse

import requests
from flask import Flask, render_template

from constants import ITEMS_API_URL, NEWS_API_URL

app = Flask(__name__)


@app.template_filter("pluralize")
def pluralize(number, singular="", plural="s"):
    if number == 1:
        return singular
    else:
        return plural


@app.template_filter("short_link")
def short_link(full_link):
    hostname = urlparse(full_link).hostname
    if hostname and hostname.startswith("www."):
        return hostname.strip("www.")

    return hostname


@app.route("/")
def home_view():
    news_response = requests.get(NEWS_API_URL)

    if not news_response.ok:
        return ("Not found - API problem", 404)

    news = news_response.json()

    return render_template("news.html", news=news)


@app.route("/<item_id>")
def item_view(item_id):
    if item_id in ["favicon.ico"]:
        return ("Not found", 404)

    item_response = requests.get(f"{ITEMS_API_URL}/{item_id}")

    if not item_response.ok:
        return ("Not found - API problem", 404)

    item = item_response.json()

    return render_template("item.html", item=item)
