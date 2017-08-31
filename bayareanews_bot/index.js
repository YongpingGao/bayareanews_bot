const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const axios = require('axios');
const config = require('./config');
const redis = require('redis');
var redisclient = redis.createClient(6379, "localhost");

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({
    extended: true
})); // for parsing application/x-www-form-urlencoded

function sendMsgToChannel(channel, msg) {
    axios.post("https://api.telegram.org/bot" + config.telegram_bot_token + "/sendMessage", {
        chat_id: channel,
        text: msg
    })
    .then(res => {
        console.log('Message posted');
    })
    .catch(err => {
        console.log('Error :', err);
    })
}

var url = "";
// Finally, start our server
app.listen(3000, function() {
    setInterval(function(){
        axios.get('https://hacker-news.firebaseio.com/v0/topstories.json')
            .then((res) => {
                return axios.get("https://hacker-news.firebaseio.com/v0/item/" + res.data[0] + ".json");
            })
            .then((res) => {
                if(url !== res.data.url) {
                    const msg =  res.data.title + '\n' + res.data.url;
                    sendMsgToChannel(config.telegram_channel, msg);
                    url = res.data.url;
                }
            })
            .catch(err => {
                console.log(err);
            });
    }, config.polling_interval);

    redisclient.subscribe("bayareanews");
    redisclient.on('message', function (channel, message) {
        if (channel == "bayareanews") {
        //    message
            sendMsgToChannel(config.telegram_channel, message);
        }
    });

    console.log('Telegram app listening on port 3000!');
});
