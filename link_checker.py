import requests
import json
from tqdm import tqdm

LINK_JSON = "https://raw.githubusercontent.com/cdt-eth/Nouns-Center/main/api/projects.json"


def main():

    # Get link list from github
    r = requests.get(LINK_JSON)
    link_json = r.json()

    # Loop through all links
    for project in tqdm(link_json):
        url = project["url"]
        if not url:
            print("No URL for project {}".format(project["title"]))
            continue

        try:
            r = requests.get(url, timeout=10)
        except:
            print("Dead link: {}".format(url))


if __name__ == "__main__":
    main()
