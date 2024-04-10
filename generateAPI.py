import requests
from requests.models import Response
# import json

def generateAPI(function):
    returnVal = Response()


    base_url = "https://www.reddit.com/"
    data = {"grant_type": "password", "username": "epicgooseman", "password": "MadridMarathon27"}
    auth = requests.auth.HTTPBasicAuth("yhGCHuRDluWwH9Fq7Tg2TQ", "aNAKWOFVX5ET5yHtN2CzBu2zVUAAWQ")
    r = requests.post(base_url + 'api/v1/access_token',
                    data=data,
                    headers={'user-agent': 'Boris Gans by epicgooseman'},
                    auth=auth)
    d = r.json()
    token = 'bearer ' + d['access_token']
    base_url = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'User-Agent': 'Boris Gans by epicgooseman'}
    response = requests.get(base_url + '/api/v1/me', headers=headers)

    def generateSubreddits():
        payload = {'q': 'statistics', 'limit': 5, 'sort': 'relevance'}
        response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
        if response.status_code == 200:
            print("Primary Search: Success")
            return response
        return 1

    def generateContent():
        
        payload = {'q': 'space', 'limit': 5, 'sort': 'relevance'}
        response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
        if response.status_code == 200:
            print("Primary Search: Success")
            return response
        return 1


    if response.status_code == 200:
        print("API Connection: Success")

        if function == "subReddits":
            returnVal = generateSubreddits()
        elif function == "content":
            returnVal = generateContent()


    return returnVal

    