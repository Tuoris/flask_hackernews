from json import load

from flask import render_template
from livereload import Server

from app import app
from constants import NEWS_SAMPLE_FILENAME, ITEM_SAMPLE_FILENAME
from helpers import get_app_host_and_port


@app.route("/debug/")
def home_debug_view():
    with open(NEWS_SAMPLE_FILENAME) as news_file:
        news = load(news_file)

    return render_template("news.html", news=news)


@app.route("/debug/<item_id>")
def item_debug_view(item_id):
    print(item_id)

    with open(ITEM_SAMPLE_FILENAME) as item_file:
        item = load(item_file)

    return render_template("item.html", item=item)


# app.jinja_env.auto_reload = True
# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.debug = True

server = Server(app.wsgi_app)
host, port = get_app_host_and_port(app)
server.serve(host="0.0.0.0", port=port)
