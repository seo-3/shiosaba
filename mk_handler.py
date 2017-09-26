import boto3
import json
import yaml
from twilio.rest import Client
from os import getenv

AWS_S3_BUCKET_NAME = getenv('BUCKET_NAME')
ACCOUNT_SID = getenv('ACCOUNT_SID')
AUTH_TOKEN = getenv('AUTH_TOKEN')
FROM = getenv('FROM')
URL = getenv('URL')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def load_config():

	s3 = boto3.resource('s3')
	res = s3.Object(AWS_S3_BUCKET_NAME, 'config.yml').get()
	body = res['Body'].read()

	return yaml.load_all(body.decode('utf-8'))

def call(to):

	client = Client(ACCOUNT_SID, AUTH_TOKEN)

	call = client.api.account.calls\
			      .create(to=to,
			              from_=FROM,
			              url=URL)

	return call.sid

def lambda_handler(event, context):

	print("Received event: " + json.dumps(event, indent=2))

	body = json.loads(event['body'])

	if 'alert' not in body or body['alert']['status'] != 'critical':
		return respond(None, event)

	service = None
	if 'service' in body :
		service = body['service']['name']
	elif 'host' in body :
		service = body['host']['roles'][0]['serviceName']

	payload = {'sid':[]}
	for data in load_config():
		if service == data['service']:
			for to in data['notifications']:
				payload['sid'].append(call(to=to["tel"]))

	return respond(None, payload)

if __name__ == "__main__":

	f = open("event.json", "r")
	event = json.load(f)
	context = ""
	f.close()

	lambda_handler(event, context)
