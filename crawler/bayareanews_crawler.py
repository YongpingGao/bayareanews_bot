#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import redis
import schedule
import time

# nohup ./bayareanews_crawler.py &

# init...
redis_host = "localhost"
redis_port = "6379"
basic_url = "https://wanqu.co"
channel_name = "bayareanews"
day_urls = []
external_urls = []
schd = "00:00"

def job():
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

    # get main page, prepare related urls
    r = requests.get(basic_url)
    r.encoding="utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.select("h2 a"):
        day_urls.append(basic_url + link.get("href"))
    for link in soup.find_all(attrs={"rel": "external"}):
        external_urls.append(link.get('href'))


    # parse each url, process and publish message to redis channel
    for i, url in enumerate(day_urls):
        r = requests.get(url)
        r.encoding="utf-8"
        soup = BeautifulSoup(r.text, "html.parser")
        # prepare data to be published
        data = external_urls[i] + '\n'
        for content in soup.select(".lead p"):
            data += content.text + '\n'
        redis_client.publish(channel_name, data)


schedule.every().day.at(schd).do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
