import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("cly7Lyd4Z3TB9/fe/Q6Tw0WdjaI97pUxEu8Psvakl3hOgUHpDb+Tdu6XbAkuMqfW7Yn75XOAchAkcVXQBFM/V0XW+jfEavlSHVdcHZiq4QkiYiUfrrU+U+PCjTd+aamsyyJSzjy5Lv+c1eGeE2fu6QdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("ed3e116a06c707a2f8fb182078f33cbb"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
