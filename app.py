from json import load

from flask import Flask, render_template

from constants import ITEM_SAMPLE_FILENAME, NEWS_SAMPLE_FILENAME

app = Flask(__name__)


@app.template_filter("pluralize")
def pluralize(number, singular="", plural="s"):
    if number == 1:
        return singular
    else:
        return plural


@app.route("/")
def home_view():
    with open(NEWS_SAMPLE_FILENAME, "r") as news_page_file:
        news = load(news_page_file)
    return render_template("news.html", news=news)


@app.route("/<item_id>")
def item_view(item_id):
    print(item_id)
    with open(ITEM_SAMPLE_FILENAME, "r") as item_page_file:
        item = load(item_page_file)
    return render_template("item.html", item=item)
