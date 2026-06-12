from fastapi import APIRouter
from app.services.worldcup import get_games, get_stadiums

router = APIRouter()

def parse_scorers(scorers):

    if scorers is None:
        return []

    if scorers == "null":
        return []

    if isinstance(scorers, list):
        return scorers

    if isinstance(scorers, str):

        scorers = scorers.strip("{}")

        if not scorers:
            return []

        return [
            scorer.strip('"')
            for scorer in scorers.split(",")
        ]

    return []

@router.get("/matches")
def get_matches(teams: str | None = None):

    data = get_games()
    stadiums = get_stadiums()

    stadium_lookup = {
    stadium["id"]: stadium["name_en"]
    for stadium in stadiums["stadiums"]
}

    matches = []

    for game in data.get("games", []):

        matches.append(
            {
                "id": game.get("id"),
                "home_team": game.get("home_team_name_en"),
                "away_team": game.get("away_team_name_en"),
                "group": game.get("group"),
                "matchday": game.get("matchday"),
                "date": game.get("local_date"),
                "stadium": stadium_lookup.get(
                    game.get("stadium_id"),
                        "Unknown Stadium"
                        ),
                "finished": game.get("finished"),
                "time_elapsed": game.get("time_elapsed"),
                "type": game.get("type"),
                "home_score": game.get("home_score"),
                "away_score": game.get("away_score"),
                "home_scorers": parse_scorers(game.get("home_scorers")),
                "away_scorers": parse_scorers(game.get("away_scorers"))
            }
        )

    if teams:

        team_set = {
            team.strip().lower()
            for team in teams.split(",")
        }

        matches = [
            match
            for match in matches
            if (
                (match["home_team"] or "").lower() in team_set
                or
                (match["away_team"] or "").lower() in team_set
            )
        ]

    return matches