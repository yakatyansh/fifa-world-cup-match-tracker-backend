from fastapi import APIRouter
import json


router = APIRouter()

@router.get("/teams")
def get_teams():

    with open("data/matches.json", "r", encoding="utf-8") as f:
        matches = json.load(f)

    teams = set()

    for match in matches:
        teams.add(match["home_team"])
        teams.add(match["away_team"])

    return sorted(list(teams))