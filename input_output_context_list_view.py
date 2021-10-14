from flask.signals import request_finished
import pyodbc
#from Database_sql import*
from flask import Flask, request, make_response, jsonify
from typing import Any, Dict, List, Optional, Text
from warnings import warn
from dialogflow_fulfillment.rich_responses import card
from flask import Flask
from flask.helpers import make_response
from flask.json import jsonify
import requests
from flask.globals import request
from dialogflow_fulfillment import Card
from pydialogflow_fulfillment import DialogflowResponse
from dialogflow_fulfillment import QuickReplies, WebhookClient
from logging import INFO
from typing import Dict
import jwt
from flask import Flask, request
from flask.logging import create_logger
#import numpy as np
from dialogflow_fulfillment import WebhookClient
app = Flask(__name__)
logger = create_logger(app)
logger.setLevel(INFO)

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook() :
    print("---------------------------------------------------------------------------------------------------------------------")
    #use WebhookClient to get agent
    request_ = request.get_json(force=True)
    #get json data in user request
    qr=request_ ['queryResult']
   
    queryText=qr['queryText']
    querys=str(queryText)
    print("querys\n\n")
    print(querys)
     # Log request headers and body
    logger.info(f'-----------------------------testing list response-------------------------------------')
    logger.info(f'Request headers: {dict(request.headers)}')
    logger.info(f'Request body   : {request_}')
    logger.info(f'------------------------------------end list program------------------------------')
    #api call - get company and make into this model.
    arr=["Aosta Software PVT","AOSTA","ASTIL"]
    sales_arr=["Total Sales","OP Sales","IP Sales","GRN","Stock","Near Expiry"]
    sub_menu=['BILLING DASHBOARD (102)', 'LAB DASHBOARD (74)', 'INVENTORY DASHBOARD (44)', 'PHARMACY DASHBOARD (33)', 'WSALE DASHBOARD (26)', 'CARDIOLOGY DASHBOARD (18)', 'DB COMPANY RIGHTS (9)', 'DB ACTIVE USERS (7)', 'DB CHANGE PASSWORD (6)', 'DB USERS ACTIVITY LOG (3)', 'DB COMPANY RIGHTS', 'DB CHANGE PASSWORD', 'DB ACTIVE USERS', 'DB USERS ACTIVITY LOG', 'DB COMPANY HOME MENU', 'NOTIFICATION GROUP', 'DB NOTIFICATION', 'ALL DASHBOARD', 'CSSD DASHBOARD', 'BILLING DASHBOARD', 'INVENTORY DASHBOARD', 'PHARMACY DASHBOARD', 'WSALE DASHBOARD', 'PWS COMPANYWISE DETAILS', 'COLLECTION DASHBOARD', 'CONTINUOUS QUALITY IMPROVEMENT', 'WS STOCK LIST', 'LAB DASHBOARD', 'CARDIOLOGY DASHBOARD', 'RADIOLOGY DASHBOARD', 'OT DASHBOARD', 'LAB DETAILS', 'PATIENT DASHBOARD', 'DEPARTMENT CHART', 'PATIENT STATS MAP', 'DEPT STATS MAP', 'PATIENT CENSUS', 'NURSING DASHBOARD', 'BED OCCUPENCY', 'COMPANYWISE DETAILS', 'COMPANYWISE HEADER DETAILS', 'BUDGET DB', 'NABH CONTINOUS QUALITY IMPROVEMENT', 'NABH HOME']
    if(querys=="GOOGLE_ASSISTANT_WELCOME"):
        option_intent(arr,queryText)
    elif(querys!="GOOGLE_ASSISTANT_WELCOME"):
        originalDetectIntentRequest=request_['originalDetectIntentRequest']
        payload=originalDetectIntentRequest['payload'] 
        input=payload['inputs']
        firstIndex=input[0]
        rawInputs=firstIndex['rawInputs']
        rawInputFirstIndex = rawInputs[0]
        #print(rawInputFirstIndex)
        query=rawInputFirstIndex['query']
        
        ###############
        for arr_i in arr:
            if(query==arr_i):
                carr_sub_menu=[]
                for sub in sub_menu:
                    carr_sub_menu.append[{'optionInfo':{'key':sub},'description':sub,'title': sub}]
                option_intent(carr_sub_menu,query)
        ############
      
def option_intent(arr,query):
    request_ = request.get_json(force=True)
    #get json data in user request
    qr=request_ ['queryResult']
    outputContexts=qr['outputContexts']
    outputContextsindex=outputContexts[0]
    parameters=outputContextsindex['parameters']
    Company_name=parameters['text']
    OPTION=parameters['OPTION']
    for i in arr:
        carr_sub_men_click=[{'optionInfo':{'key':'1'},'description':i,'title':i}]
    cmp={
                                        "payload": {
                                            "google": {
                                                "expectUserResponse": True,
                                                "richResponse": {
                                                    "items": [
                                                    {
                                                        "simpleResponse": {
                                                                "textToSpeech": "Choose a items"
                                                            }
                                                            }
                                                            ]                                        },
                                                                "systemIntent": {
                                                                    "intent": "actions.intent.OPTION",
                                                                    "data": {
                                                                    "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
                                                                    "listSelect": {
                                                                        "title": "you are selecting ",
                                                                        "items": carr_sub_men_click
                                                                    }
                                                                    }
                                                                }
                                                                }
                                                            }
                                                            }
    return cmp
if __name__ == '__main__':
    app.run()