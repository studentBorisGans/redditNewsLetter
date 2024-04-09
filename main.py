import requests
base_url = "https://www.reddit.com/"
data = {"grant_type": "password", "username": "epicgooseman", "password": "MadridMarathon27"}
auth = requests.auth.HTTPBasicAuth("yhGCHuRDluWwH9Fq7Tg2TQ", "aNAKWOFVX5ET5yHtN2CzBu2zVUAAWQ")
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'Boris Gans by epicgooseman'},
		          auth=auth)
# yhGCHuRDluWwH9Fq7Tg2TQ
d = r.json()
token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'Boris Gans by epicgooseman'}
response = requests.get(base_url + '/api/v1/me', headers=headers)
# api_url = base_url + "/api/v1/me"

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])

payload = {'q': 'donald trump', 'limit': 5, 'sort': 'relevance'}
response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
print(response.status_code)

values = response.json()
# print(response.text)

for i in range(len(values['data']['children'])):
    print(values['data']['children'][i]['data']['display_name'])

