import requests

response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

print(response.status_code)

data = response.json()

print(data.keys())

print(type(data["elements"]))
print(len(data["elements"]))
print(data["elements"][0].keys())