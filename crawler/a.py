#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import redis
import schedule
import time
import argparse

# nohup ./bayareanews_crawler.py &


def job():
    day_urls = []

    day_urls.append(1)
    day_urls.append(2)
    day_urls.append(3)

    print len(day_urls)


schedule.every(2).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)  # wait one minute
