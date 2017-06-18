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
client = pymongo.MongoClient(uri)

db = client.get_default_database()


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
        elif tag == 1:
            for doc in scenes.find():
                if u'台北' in doc['Add'] or u'臺北' in doc['Add']:
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
        elif tag == 2:
            for doc in scenes.find():
                if u'台中' in doc['Add'] or u'臺中' in doc['Add']:
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
        elif tag == 3:
            for doc in scenes.find():
                if u'台東' in doc['Add'] or u'臺東' in doc['Add']:
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
        elif tag == 4:
            for doc in scenes.find():
                if u'桃園' in doc['Add']:
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
        elif tag == 5:
            for doc in scenes.find():
                if u'新竹' in doc['Add']:
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
        elif tag == 6:
            for doc in scenes.find():
                if u'苗栗' in doc['Add']:
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
        elif tag == 7:
            for doc in scenes.find():
                if u'彰化' in doc['Add']:
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
        elif tag == 8:
            for doc in scenes.find():
                if u'南投' in doc['Add']:
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
        elif tag == 9:
            for doc in scenes.find():
                if u'雲林' in doc['Add']:
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
        elif tag == 10:
            for doc in scenes.find():
                if u'嘉義' in doc['Add']:
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
        elif tag == 11:
            for doc in scenes.find():
                if u'高雄' in doc['Add']:
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
        elif tag == 12:
            for doc in scenes.find():
                if u'屏東' in doc['Add']:
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
        elif tag == 13:
            for doc in scenes.find():
                if u'宜蘭' in doc['Add']:
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
        elif tag == 14:
            for doc in scenes.find():
                if u'花蓮' in doc['Add']:
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


def upload_flag(flag, sender_id):
    Category = db['flag']
    query = {'ID': sender_id}
    if(Category.count(query) == 0):
        Category.insert_one({'ID': sender_id, 'flag': flag})
    else:
        query = {'ID': sender_id}
        Category.update(query, {'$set': {'flag': flag}})


def get_flag(sender_id):
    Category = db['flag']
    dat = Category.find_one({'ID': sender_id})
    return dat['flag']


def upload_db_photo_url(url, sender_id):
    Postcard = db['postcard']
    query = {'ID': sender_id}
    if(Postcard.count(query) == 0):
        SEED_DATA = {
            'url': url,
            'ID': sender_id
        }
        print Postcard.insert_one(SEED_DATA)
    else:
        Postcard.update(query, {'$set': {'url': url}})


def upload_db_intro(text, sender_id):
    Postcard = db['postcard']
    query = {'ID': sender_id}
    Postcard.update(
        query, {'$set': {'intro': text, 'match': '0', 'match_id': "None"}})
    client.close()


def get_mail(my_id):
    Postcard = db['postcard']
    query = {'ID': my_id}
    my_data = Postcard.find_one(query)
    sender_id = my_data['match_id']
    query = {'ID': sender_id}
    data = Postcard.find_one(query)
    return data
