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
                    "message":{
                        "attachment":{
                                "type":"template",
                                "payload":{
                                            "template_type":"generic",
                                            "elements":[
                                                    ]
                                            }
                                    }
                                }
                }
    return(template)
def add_template(template,title,description):
    #add new information in to the template
    bobble={
        "title":title,
        "subtitle":description,
        
        } 
    template["message"]["attachment"]["payload"]["elements"].append(bobble)
    return template