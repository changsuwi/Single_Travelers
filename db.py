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

def main(args):

    client = pymongo.MongoClient(uri)

    db = client.get_default_database()
    
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.

    scenes = db['travel']
    for doc in scenes.find({'Gov':'315080900H'}):
        if(u"琉球鄉" in doc['Add']):
            print doc['Name'].encode('utf-8')
            
if __name__ == '__main__':
    main(sys.argv[1:])