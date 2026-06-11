from fastapi import APIRouter
from app.services.worldcup import get_games

router = APIRouter()


@router.get("/matches")
def get_matches(teams: str | None = None):

    data = get_games()

    matches = []

    for game in data["games"]:
        matches.append(
            {
                "id": game["id"],
                "home_team": game["home_team_name_en"],
                "away_team": game["away_team_name_en"],
                "group": game["group"],
                "matchday": game["matchday"],
                "date": game["local_date"],
                "stadium_id": game["stadium_id"],
                "finished": game["finished"],
                "time_elapsed": game["time_elapsed"],
                "type": game["type"],
                "home_score": game["home_score"],
                "away_score": game["away_score"]
            }
        )

    if teams:

        team_list = [
            team.strip()
            for team in teams.split(",")
        ]

        matches = [
            match
            for match in matches
            if (
                match["home_team"] in team_list
                or match["away_team"] in team_list
            )
        ]

    return matches