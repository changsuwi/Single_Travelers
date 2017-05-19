# -*- coding: utf-8 -*-
"""
Created on Sat May 06 01:36:19 2017

@author: vic
"""

# coding=utf-8
from sendtofb_log import log
from json_fb import json_message, json_mainbutton, json_location, json_photo
from db import search_scene, upload_db_photo_url, upload_db_intro, upload_flag, get_flag, get_mail
import os
from imgur import upload_photo


from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events
    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing
    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]

                if messaging_event.get("message"):  # someone sent us a message
                    if("quick_reply" in messaging_event["message"]):
                        payload = messaging_event["message"][
                            "quick_reply"]["payload"]
                        if(payload == "mainbutton_1"):
                            upload_flag(1, sender_id)
                            json_message(sender_id, '你可以直接輸入地點詢問,例如')
                            json_message(sender_id, '我想找台南的景點')
                            json_message(sender_id, '或是分享你的地點，來獲得離你最近的景點資訊')
                            json_location(sender_id)
                        elif payload == "mainbutton_4":
                            upload_flag(4, sender_id)
                            json_message(
                                sender_id, '旅行明信片是一個特別的社交方式，藉由互送明信片，分享旅途的美麗風景，認識其他熱愛旅行的旅人！')
                            json_message(sender_id, "請先傳送一張旅途的美麗風景，作為明信片的封面吧~")
                    elif("text" in messaging_event["message"]):
                        message_text = messaging_event["message"][
                            "text"]  # the message's text
                        print(sender_id)  # test
                        if(message_text == "Hello" or message_text == "Hi" or message_text == u"嗨" or message_text == u"妳好" or message_text == u"你好" or message_text == "hello" or message_text == "hi" or message_text == u"哈囉"):

                            json_message(sender_id, "你好，我是旅行助理。專為愛旅行的你所打造!")
                            json_mainbutton(sender_id)
                        elif u'台南' in message_text and get_flag(sender_id) == 1:
                            search_scene(sender_id, 0, 0, 0, 1, 0)
                        elif get_flag(sender_id) == 4:
                            upload_db_intro(message_text, sender_id)
                            json_message(sender_id, "已完成，請耐心等待神秘的明信片")

                    elif("attachments" in messaging_event["message"]):
                        attachment = messaging_event["message"]["attachments"]
                        if(attachment[0]["type"] == u"location"):

                            px = float(attachment[0]["payload"][
                                       "coordinates"]["long"])
                            py = float(attachment[0]["payload"][
                                       "coordinates"]["lat"])
                            search_scene(sender_id, px, py, 0, 0, 0)
                        elif(attachment[0]["type"] == u"image"):
                            for attachment in messaging_event["message"]["attachments"]:
                                url = attachment["payload"]["url"]
                            url = upload_photo(url)
                            upload_db_photo_url(url, sender_id)
                            json_message(sender_id, "已收到圖片")
                            json_message(
                                sender_id, "請輸入簡單的明信片內容，給未知的旅行愛好者吧\n 例如")
                            json_message(sender_id, "嗨～這是美麗的西子灣秘境，分享給妳~")

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                # user clicked/tapped "postback" button in earlier message
                if messaging_event.get("postback"):
                    if 'http' in messaging_event["postback"]["payload"]:
                        place_url = messaging_event["postback"]["payload"]
                        json_message(sender_id, place_url)
                    else:
                        wantwatch = messaging_event[
                            "postback"]["payload"].split()
                        if len(wantwatch) == 3:
                            px = float(wantwatch[0])
                            py = float(wantwatch[1])
                            count = int(wantwatch[2])
                            search_scene(sender_id, px, py, count, 0, 0)
                        else:
                            tag = int(wantwatch[0])
                            count = int(wantwatch[1])
                            search_scene(sender_id, 0, 0, count, 1, tag)

    return "ok", 200


if __name__ == '__main__':
    app.run(debug=True)
