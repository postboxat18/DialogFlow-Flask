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
        dialogflow_response = DialogflowResponse("welcome")
        print("Response:\n\n"+dialogflow_response.get_final_response())
        people=dialogflow_response.get_final_response()
        #print(people)
        return people
    elif(querys!="GOOGLE_ASSISTANT_WELCOME"):
        outputContexts=qr['outputContexts']
        outputContextsindex=outputContexts[0]
        parameters=outputContextsindex['parameters']
        planet=parameters['planet']
        attribute=parameters['attribute']
        dialogflow_response = DialogflowResponse("your "+attribute+" of "+planet)
        print("Response:\n\n"+dialogflow_response.get_final_response())
        people=dialogflow_response.get_final_response()
        #print(people)
        return people
if __name__ == '__main__':
    app.run()