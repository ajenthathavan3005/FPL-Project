import requests
import pandas as pd


def getData(apiEndpoint):
    response = requests.get(apiEndpoint)
    data = response.json()

    players_df = pd.DataFrame(data["elements"])

    return data, players_df


def getId(playerName, players_df):
    full_name = (
        players_df["first_name"] + " " + players_df["second_name"]
    )

    player = players_df[
        (players_df["known_name"] == playerName) |
        (full_name == playerName)
    ]

    if player.empty:
        return None

    return player.iloc[0]["id"]


def getPlayerInfo(playerId, players_df):
    player = players_df[
        players_df["id"] == playerId
    ]

    if player.empty:
        return None

    return player.iloc[0]


def comparePlayers(player1, player2):
    stats = [
        "total_points",
        "goals_scored",
        "assists",
        "minutes"
    ]

    player1_name = (
        player1["known_name"]
        or player1["first_name"] + " " + player1["second_name"]
    )

    player2_name = (
        player2["known_name"]
        or player2["first_name"] + " " + player2["second_name"]
    )

    comparison = pd.DataFrame({
        player1_name: [player1[stat] for stat in stats],
        player2_name: [player2[stat] for stat in stats]
    }, index=stats)

    return comparison


data, players_df = getData(
    "https://fantasy.premierleague.com/api/bootstrap-static/"
)


palmer_id = getId("Cole Palmer", players_df)
bruno_id = getId("Bruno Fernandes", players_df)

palmer = getPlayerInfo(palmer_id, players_df)
bruno = getPlayerInfo(bruno_id, players_df)

comparison = comparePlayers(palmer, bruno)

print(comparison)