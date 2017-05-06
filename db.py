# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:09:05 2017

@author: vicharm
"""

# -*- coding:utf-8 -*-
import sys
import pymongo
### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
uri = 'mongodb://vic010744:vic32823@ds023455.mlab.com:23455/heroku_xfc3zss3' 

###############################################################################
# main
###############################################################################

def search_scene(px,py):

    client = pymongo.MongoClient(uri)

    db = client.get_default_database()
    
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.

    scenes = db['travel']
    for doc in scenes.find():
        if(pow(float(doc['Px']) - px ,2) + pow(float(doc['Py']) - py ,2)< 0.01):
            print doc['Name'].encode('utf-8')
            
