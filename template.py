# -*- coding: utf-8 -*-
"""
Created on Sat May 06 20:42:58 2017

@author: vicharm
"""


def new_template(sender_id):
    template = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                    ]
                }
            }
        }
    }
    return template


def add_template(template, title, description, image_url, px, py, count):
    # add new information in to the template
    if(title == u'想看更多?'):
        bobble = {
            "title": title,
            "image_url": image_url,
            "subtitle": description,
            "button":
            [
                {
                    "type": "postback",
                    "title": "看更多",
                    "payload": str(px) + " " + str(py) + " " + str(count)
                }
            ]
        }

    else:
        bobble = {
            "title": title,
            "image_url": image_url,
            "subtitle": description
        }
    template["message"]["attachment"]["payload"]["elements"].append(bobble)
    return template
