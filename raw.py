Connect & Disconnect

import json

def lambda_handler(event, context):
    print(event)
    print("****")
    print(context)


SendMessage - Needs AmazonAPIGatewayInvokeFullAccess IAM Policy

import json
import urllib3
import boto3

client = boto3.client('apigatewaymanagementapi', endpoint_url="xxxxxxxxxx.com/production")

def lambda_handler(event, context):
    print(event)
    
    #Extract connectionId from incoming event
    connectionId = event["requestContext"]["connectionId"]
    
    #Do something interesting... 
    responseMessage = "responding..."
    
    #Form response and post back to connectionId
    response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(responseMessage).encode('utf-8'))
    return { "statusCode": 200  }


Broadcast - Needs AmazonAPIGatewayInvokeFullAccess IAM Policy

import json
import urllib3
import boto3

client = boto3.client('apigatewaymanagementapi', endpoint_url="xxxxxx.com/production")

def lambda_handler(event, context):
    
    #Extract connectionId and desired message to send from input
    connectionId = event["connectionId"]
    message = event["message"]
    
    #Form response and post back to provided connectionId
    response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(message).encode('utf-8'))
    print(response)
    
 Broadcast Lambda Input Event Example

{
  "connectionId": "FUVNdckkIAMCIZw=",
  "message": "Anyone out there?"
}

