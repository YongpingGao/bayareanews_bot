#!/usr/env/bin

echo "start redis server..."
redis-server&

echo "schedule crawling..."

crawler/bayareanews_crawler.py&

echo "start server..."
pm2 start bayareanews_bot/index.js&


