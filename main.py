import json

from generateAPI import generateAPI

response = generateAPI("subReddits")
values = response.json()

print("\n")
for i in range(len(values['data']['children'])):
    print(values['data']['children'][i]['data']['display_name'])

with open("redditSubreddits.json", "w") as file:
    json.dump(values, file)


with open("redditContent.json", "w") as file:
    json.dump(values, file)





# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }

# json_file = json.load("redditData.json")

# with open("redditContent.json", "w") as file:
#     json.dump(dictionary, file)

# /api/v1/collections/collection