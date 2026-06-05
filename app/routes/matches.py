from fastapi import APIRouter
import json

router = APIRouter()


@router.get("/matches")
def get_matches(teams: str | None = None):

    with open("data/matches.json", "r", encoding="utf-8") as f:
        matches = json.load(f)
    if teams:

        team_list = [team.strip() for team in teams.split(",")]


        matches = [
            match
            for match in matches
            if (
                match["home_team"] in team_list
                or match["away_team"] in team_list
            )
            
        ]

    return matches