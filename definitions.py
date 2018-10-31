import time
import requests
import json

from tts import talk

BASE_REDDIT_URL = 'http://www.reddit.com/r/'
JSON_FILE_PATH = '/data/pastSearches.json'
SUCCESS_CODE = 200
TOO_MANY_REQUESTS_EXCEPTION = 429

start=time.time()

def begin(args):
	while True:
		searchReddit(args)
		time.sleep(args['t'] - ((time.time() - start) % args['t']))

def generateSearchUrl(args):
	return BASE_REDDIT_URL + args['s'] + '/search.json?q=' + args['p'] + '&restrict_sr=on&sort=new' 

def getJsonFromFile():
	with open(JSON_FILE_PATH) as file:
		data = json.load(file)
	return data;
def parseJson(childrenJson):
	for child in childrenJson:
		child


def searchReddit(args):
	print(generateSearchUrl(args))
	r = requests.get(generateSearchUrl(args))
	if(r.status_code == SUCCESS_CODE):
		subredditFilter(args, r.json()['data']['children'])
	elif(r.status_code == TOO_MANY_REQUESTS_EXCEPTION):
		print('Sent too many requests, retrying next tick.')
	else:
		print('Unexpected Error, retrying next tick')
		print(r.json())



