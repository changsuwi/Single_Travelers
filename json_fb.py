# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:50:20 2017
json_fb 此模組主要存放通用的json格式與打包 
例如使用者輸入json , template打包 ， main button 的json ，message的打包
@author: vicharm
"""
from sendtofb_log import sendtofb, log
import json


def get_start():
    data = json.dumps(
        {
            "get_started":
            {
                "payload": "GET_STARTED_PAYLOAD"
            }
        })
    sendtofb(data)


def set_manu():
    data = json.dumps(
        {
            "persistent_menu": [
                {
                    "locale": "default",
                    "composer_input_disabled": False,
                    "call_to_actions": [
                        {
                              "title": u"聊天",
                              "type": "postback",

                        },
                        {
                            "type": "postback",
                            "title": u"交換明信片",
                        },
                        {
                            "type": "postback",
                            "title": u"可愛寵物影片推播",
                        },
                        {
                            "type": "nested",
                            "title": u"領養資訊搜尋",
                            "call_to_actions": [
                                {
                                    "title": "Pay Bill",
                                    "type": "postback",
                                    "payload": "PAYBILL_PAYLOAD"
                                },
                                {
                                    "title": "History",
                                    "type": "postback",
                                    "payload": "HISTORY_PAYLOAD"
                                }

                            ]
                        },
                        {
                            "locale": "zh_CN",
                            "composer_input_disabled": False
                        }
                    ]
                }
            ]
        }
    )
    sendtofb(data)


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
                    "title": "美食搜尋",
                    "payload": "mainbutton_2"
                },
                {
                    "content_type": "text",
                    "title": "住宿搜尋",
                    "payload": "mainbutton_3"
                },
                {
                    "content_type": "text",
                    "title": "旅伴明信片",
                    "payload": "mainbutton_4"
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
