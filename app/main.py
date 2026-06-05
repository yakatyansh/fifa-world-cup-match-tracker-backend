from fastapi import FastAPI
from app.routes.matches import router as matches_router
from app.routes.teams import router as teams_router


app = FastAPI()

app.include_router(matches_router)
app.include_router(teams_router)


@app.get("/health")
def health():
    return {"status": "healthy"}