# Marvel characters have a power grid at
# https://marvel.fandom.com/wiki/Power_Grid
# This application scrapes it into a CSV file with columns: name, url, power, value

import pandas as pd
import requests
from lxml.html import fromstring


def get_power_grid():
    url = "https://marvel.fandom.com/wiki/Power_Grid"
    response = requests.get(url)
    tree = fromstring(response.content)
    links = tree.cssselect("#mw-content-text a")
    last_power, last_value, level = None, None, 0
    for link in links:
        href = link.get("href", "")
        if href.startswith("/wiki/Category:Power_Grid/") and href.count("/") == 4:
            parts = href.split("/")
            power, value = parts[3], parts[4]
            if power == last_power:
                if value != last_value:
                    last_value, level = value, level + 1
            else:
                last_power, last_value, level = power, level, 1
            yield {"value": value, "power": power, "url": href, "level": level}


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
                    "level": item["level"],
                }
            next_link = tree.cssselect(".category-page__pagination-next")
            if len(next_link) == 0:
                break
            else:
                url = next_link[0].get("href", "")


def scrape():
    data = pd.DataFrame(get_powers())
    data["url"] = "https://marvel.fandom.com" + data["url"]
    data.to_csv("marvel-powers.csv", index=False)
    powers = data.pivot_table(
        index=["name", "url"],
        columns=["power"],
        values="level",
        aggfunc=["min", "max"],
        sort=True,
    )
    powers.columns = [" ".join(col).strip() for col in powers.columns.values]
    powers = powers.reset_index()
    powers.to_csv("marvel-powers-summary.csv", index=False)
    with open("marvel-powers-summary.json", "w") as handle:
        handle.write(powers.to_json(orient="records", indent=2))


if __name__ == "__main__":
    scrape()
