import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

URL = "https://www.koreafilm.or.kr/kofa/news/recruit"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

post = soup.select_one("table tbody tr td a")
title = post.text.strip()
link = "https://www.koreafilm.or.kr" + post["href"]

with open("last_post.txt", "r") as f:
    old = f.read().strip()

if title != old:

    sender = os.environ["EMAIL_ID"]
    password = os.environ["EMAIL_PW"]
    receiver = os.environ["EMAIL_TO"]

    msg = MIMEText(f"새 채용 공고 올라옴\n\n{title}\n{link}")
    msg["Subject"] = "KOFA 채용 공고 알림"
    msg["From"] = sender
    msg["To"] = receiver

    smtp = smtplib.SMTP_SSL("smtp.naver.com", 465)
    smtp.login(sender, password)
    smtp.send_message(msg)
    smtp.quit()

    with open("last_post.txt", "w") as f:
        f.write(title)
