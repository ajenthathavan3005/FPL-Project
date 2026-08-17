import requests

def getData(apiEndpoint):
    response = requests.get(apiEndpoint)
    data = response.json()
    return data

def getPlayerInfo(playerNameFirst, playerNameLast, data):
    for player in data["elements"]:
        if player["first_name"] == playerNameFirst and player["second_name"] == playerNameLast:
            return player



data = getData("https://fantasy.premierleague.com/api/bootstrap-static/")
print(data.keys())

palmer = getPlayerInfo("Cole", "Palmer", data)

print(palmer)
print(palmer["goals_scored"])
print(palmer["assists"])
print(palmer["total_points"])
    