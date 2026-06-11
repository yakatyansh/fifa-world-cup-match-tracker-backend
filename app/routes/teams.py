from fastapi import APIRouter
from app.services.worldcup import get_teams as fetch_teams

router = APIRouter()


@router.get("/teams")
def get_teams():

    data = fetch_teams()

    return data["teams"]