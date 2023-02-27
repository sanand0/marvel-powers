# Marvel characters have a power grid at
# https://marvel.fandom.com/wiki/Power_Grid
# This application scrapes it into a CSV file with columns: name, url, power, value

import csv
import requests
from lxml.html import fromstring


def get_power_grid():
    url = "https://marvel.fandom.com/wiki/Power_Grid"
    response = requests.get(url)
    tree = fromstring(response.content)
    links = tree.cssselect("#mw-content-text a")
    for link in links:
        href = link.get("href", "")
        if href.startswith("/wiki/Category:Power_Grid/") and href.count("/") == 4:
            parts = href.split("/")
            yield {"value": link.text_content(), "power": parts[3], "url": href}


def get_powers():
    for item in get_power_grid():
        url = "https://marvel.fandom.com" + item["url"]
        while True:
            print(url)
            response = requests.get(url)
            tree = fromstring(response.content)
            links = tree.cssselect("#mw-content-text .category-page__member-link")
            for link in links:
                yield {
                    "name": link.text_content(),
                    "url": link.get("href", ""),
                    "value": item["value"],
                    "power": item["power"],
                }
            next_link = tree.cssselect(".category-page__pagination-next")
            if len(next_link) == 0:
                break
            else:
                url = next_link[0].get("href", "")


def scrape():
    with open("marvel.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "url", "power", "value"])
        writer.writeheader()
        for item in get_powers():
            writer.writerow(item)


if __name__ == "__main__":
    scrape()
