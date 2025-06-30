import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('last hello from CICD Lambda again!')
        }