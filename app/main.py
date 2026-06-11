from fastapi import FastAPI
from app.routes.matches import router as matches_router
from app.routes.teams import router as teams_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fifa-world-cup-match-tracker-fronte.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(matches_router)
app.include_router(teams_router)


@app.get("/health")
def health():
    return {"status": "healthy"}