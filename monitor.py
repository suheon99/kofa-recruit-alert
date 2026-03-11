import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

URL = "https://www.koreafilm.or.kr/kofa/news/recruit"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

title = soup.select_one("table tbody tr td a").text.strip()
link = soup.select_one("table tbody tr td a")["href"]

with open("last_post.txt", "r") as f:
    old = f.read().strip()

if title != old:

    sender = os.environ["EMAIL_ID"]
    password = os.environ["EMAIL_PW"]
    receiver = os.environ["EMAIL_TO"]

    msg = MIMEText(f"새 채용 공고 올라옴\n\n{title}\nhttps://www.koreafilm.or.kr{link}")
    msg["Subject"] = "KOFA 채용 공고 알림"
    msg["From"] = sender
    msg["To"] = receiver

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, password)
    smtp.send_message(msg)
    smtp.quit()

    with open("last_post.txt", "w") as f:
        f.write(title)
