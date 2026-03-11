import requests
from bs4 import BeautifulSoup

URL = "https://www.koreafilm.or.kr/kofa/news/recruit"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

title = soup.select_one("table tbody tr td a").text.strip()

with open("last_post.txt", "r") as f:
    old = f.read().strip()

if title != old:
    print("NEW POST:", title)

    with open("last_post.txt", "w") as f:
        f.write(title)
