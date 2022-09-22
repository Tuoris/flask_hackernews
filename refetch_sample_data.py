from json import dump

import requests

from constants import (
    ITEM_SAMPLE_FILENAME,
    ITEMS_API_URL,
    NEWS_API_URL,
    NEWS_SAMPLE_FILENAME,
)


def main():
    news_response = requests.get(NEWS_API_URL)
    with open(NEWS_SAMPLE_FILENAME, "w") as news_page_file:
        dump(news_response.json(), news_page_file)

    item_id = 32850178
    item_response = requests.get(f"{ITEMS_API_URL}/{item_id}")
    with open(ITEM_SAMPLE_FILENAME, "w") as item_page_file:
        dump(item_response.json(), item_page_file)


if __name__ == "__main__":
    main()
