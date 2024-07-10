import os
import json
import socket

def lambda_handler(event, context):
    
    # print("Scenario 1");
    os.environ['_HANDLER'] = 'hello'
    # print("Scenario 1 ends")
    # print("Scenario 2");
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',0))
    # print("Scenario 2 ends")
    
    return {
        'statusCode': 200,
        'body': json.dumps("Inspector Code Scanning", default=str)
    } 
