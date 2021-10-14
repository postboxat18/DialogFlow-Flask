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
    
    if(querys=="GOOGLE_ASSISTANT_WELCOME"):
        option_intent(arr,queryText)
    elif(querys!="GOOGLE_ASSISTANT_WELCOME"):
        outputContexts=qr['outputContexts']
        outputContextsindex=outputContexts[0]
        parameters=outputContextsindex['parameters']
        Company_name=parameters['text']
        OPTION=parameters['OPTION']
        ###############
        carr_sub_menu_click=[{'optionInfo':{'key':'Total Sales'},'description':'totalSale','title':'Total Sales'},
                                            {'optionInfo':{'key':'OP Sales'},'description':'iOP_Stock_ue','title':'OP Sales'},
                                            {'optionInfo':{'key':'IP Sales'},'description':'iIP_Sales_Amt','title':'IP Sales'},
                                            {'optionInfo':{'key':'GRN'},'description':'grnTotal','title':'GRN'},
                                            {'optionInfo':{'key':'Stock'},'description':'totalStock','title':'Stock'},
                                            {'optionInfo':{'key':'Near Expiry'},'description':'totalExpiry','title':'Near Expiry'}]
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
                                                                        "title": "your "+OPTION+" of "+Company_name,
                                                                        "items": carr_sub_menu_click
                                                                    }
                                                                    }
                                                                }
                                                                }
                                                            }
                                                            }
        return cmp
        ############
        dialogflow_response = DialogflowResponse("your "+OPTION+" of "+Company_name)
        print("Response:\n\n"+dialogflow_response.get_final_response())
        people=dialogflow_response.get_final_response()
        #print(people)
        return people
def option_intent(arr,query):
    
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