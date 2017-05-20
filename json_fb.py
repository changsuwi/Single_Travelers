# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:50:20 2017
json_fb 此模組主要存放通用的json格式與打包 
例如使用者輸入json , template打包 ， main button 的json ，message的打包
@author: vicharm
"""
from sendtofb_log import sendtofb, log
import json


def typingon_json(recipient_id):

    # construct typing on json
    log("sending  typingon to {recipient}".format(recipient=recipient_id))
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "sender_action": "typing_on"})

    sendtofb(data)


def json_template(template, recipient_id):  # construct template json
    log("sending  template to {recipient}".format(recipient=recipient_id))
    data = json.dumps(template)
    sendtofb(data)


def json_mainbutton(recipient_id):  # construct mainbutton json
    log("sending mainbutton to {recipient}".format(recipient=recipient_id))
    data = json.dumps(
        {"recipient": {
            "id": recipient_id
        },
            "message": {
            "text": "請選擇您想要的服務:",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "景點搜尋",
                    "payload": "mainbutton_1"
                },
                {
                    "content_type": "text",
                    "title": "旅伴明信片",
                    "payload": "mainbutton_2"
                }

            ]
        }
        }
    )
    sendtofb(data)


def json_location(recipient_id):
    log("sending location to {recipient}".format(recipient=recipient_id))
    data = json.dumps(
        {
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": "Please share your location:",
                "quick_replies": [
                    {
                        "content_type": "location",
                    }
                ]
            }
        }
    )
    sendtofb(data)


def json_photo(recipient_id, url):
    log("sending photo to {recipient}".format(recipient=recipient_id))
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url
                }
            }
        }
    })
    sendtofb(data)


def json_message(recipient_id, message_text):  # construct message json

    log("sending message to {recipient}: {text}".format(
        recipient=recipient_id, text=message_text))
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    sendtofb(data)
