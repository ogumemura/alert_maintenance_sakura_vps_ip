#!/usr/bin/env python3
# check_mente_sakura_vps.py3 : Send an email if the specified IP address is found in Sakura VPS maintenance information.

import requests
from bs4 import BeautifulSoup
import feedparser
import smtplib
import socket
from email.message import EmailMessage
from datetime import datetime, timedelta

# Configurations
rss_url = "https://www.sakura.ad.jp/rss/mainte.rdf"  # Replace with the desired RSS URL
target_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]  # Replace with the desired IP addresses
sender_address = "sender@example.com"  # Replace with your email address
to_address = "you@example.com"

# Fetch RSS feed
feed = feedparser.parse(rss_url)

# Get articles with title containing "VPS" from the last 24 hours
current_time = datetime.now()
time_limit = current_time - timedelta(days=1)
articles = [entry for entry in feed.entries if "VPS" in entry.title and datetime(*entry.published_parsed[:6]) > time_limit]

# Check for target IPs and send email if found
for article in articles:
    page_content = requests.get(article.link).content
    soup = BeautifulSoup(page_content, "html.parser")

    matching_ips = [ip for ip in target_ips if ip in soup.text]

    if matching_ips:
        ip_and_hostnames = []
        for ip in matching_ips:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown"
            ip_and_hostnames.append(f"{ip} - {hostname}")

        msg = EmailMessage()

        msg.set_content(f"Found target IPs and hostnames in the following article: {article.link}\n\n" + "\n".join(ip_and_hostnames))
        msg["Subject"] = f" Sakura VPS maintenance information: {', '.join(matching_ips)}"

        msg["From"] = sender_address
        msg["To"] = to_address

        with smtplib.SMTP("127.0.0.1") as server:
            server.send_message(msg)

        print(f"Email sent for article: {article.link}")
    else:
        print(f"No matching IPs found in article: {article.link}")
