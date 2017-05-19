# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:09:05 2017

@author: vicharm
"""

# -*- coding:utf-8 -*-
import pymongo
import json
from sendtofb_log import log, sendtofb
from json_fb import json_message
from template import new_template, add_template
# Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
uri = 'mongodb://vic010744:vic32823@ds023455.mlab.com:23455/heroku_xfc3zss3'

###############################################################################
# main
###############################################################################


def search_scene(sender_id, px, py, count2, mode, tag):
    log("sending search_scene")
    client = pymongo.MongoClient(uri)

    db = client.get_default_database()

    # First we'll add a few songs. Nothing is required to create the songs
    # collection; it is created automatically when we insert.

    scenes = db['travel']
    template = new_template(sender_id)
    count = 0
    if mode == 0:
        for doc in scenes.find():
            if (pow(float(doc['Px']) - px, 2) + pow(float(doc['Py']) - py, 2) < 0.035):
                count = count + 1
                if(count >= count2):
                    name = doc['Name'].encode('utf-8')
                    discription = doc['Toldescribe'].encode('utf-8')
                    image_url = doc['Picture1']
                    place_url = doc['place_url']
                    if(count >= count2 + 8):
                        template = add_template(template, u"想看更多?", u"看更多", image_url, px, py, count, place_url, mode, tag)
                        break
                    else:
                        template = add_template(template, name, discription, image_url, px, py, count, place_url, mode, tag)
    else:
        if tag == 0:   # tainan
            for doc in scenes.find():
                if u'tainan' in doc['Add'] or u'台南' in doc['Add'] or u'Tainan' in doc['Add']:
                    print "in find"
                    if count >= count2:
                        name = doc['Name'].encode('utf-8')
                        discription = doc['Toldescribe'].encode('utf-8')
                        image_url = doc['Picture1']
                        place_url = doc['place_url']
                        if(count >= count2 + 8):
                            template = add_template(template, u"想看更多?", u"看更多", image_url, px, py, count, place_url, mode, tag)
                            break
                        else:
                            template = add_template(template, name, discription, image_url, px, py, count, place_url, mode, tag)
                    count = count + 1
    if count == 0 or (count < count2):
        json_message(sender_id, "嗚嗚嗚不好意思，找不到相對應的結果")
    else:
        data = json.dumps(template)
        sendtofb(data)
