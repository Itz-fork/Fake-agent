# Copyright (c) 2022 Itz-fork

from json import dump
from requests import get
from os.path import dirname
from bs4 import BeautifulSoup


def update_database():
    """
    Update local database of user agents
    """
    BROWSERS = ["Chrome", "Firefox", "Edge",
                "Opera", "Safari", "Internet Explorer"]
    
    print("Starting to update local database...\n")
    
    for browser in BROWSERS:
        print(f"\r[+] Scraping: {browser}", end="")

        resp = get(
            f"http://useragentstring.com/pages/useragentstring.php?name={browser}")
        soup = BeautifulSoup(resp.text, "html.parser")
        agents = []
        for ul in soup.find_all("div", attrs={"id": "liste"}):
            for li in ul.find_all("ul"):
                for item in li.find_all("li"):
                    agents.append(item.text)

        to_wrtie = {num: agent for num, agent in enumerate(agents)}
        with open("{}/data/{}.json".format(dirname(__file__), browser.replace(" ", "")), 'w') as f:
            dump(to_wrtie, f, indent=4)

        print(f"\x1b[2K\r[✅] Added: {len(agents)} of {browser} user agents")

    print("\n User-agents database has been updated! \n")