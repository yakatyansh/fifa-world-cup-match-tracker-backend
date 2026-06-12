from fastapi import APIRouter
from app.services.worldcup import get_teams as fetch_teams

router = APIRouter()


@router.get("/teams")
def get_teams():

    data = fetch_teams()

    return [
        {
            "id": team["id"],
            "name_en": team["name_en"],
            "flag": team["flag"],
            "iso2": team["iso2"],
            "group": team["groups"],
        }
        for team in data["teams"]
    ]