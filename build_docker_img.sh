#/usr/bin/env bash

docker build crawler/ -t crawler
docker build bayareanews_bot/ -t node_server

docker tag crawler jjasongao/telegram_bayareanews:crawler
docker tag node_server jjasongao/telegram_bayareanews:node_server

docker push jjasongao/telegram_bayareanews:crawler
docker push jjasongao/telegram_bayareanews:node_server