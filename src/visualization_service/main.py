from fastapi import FastAPI
from visualization_service.api.players import router as players_router
from visualization_service.api.standings import router as standings_router

app = FastAPI(title="Sportly Visualization Service", root_path="/api/charts")

app.include_router(players_router, prefix="/charts")
app.include_router(standings_router, prefix="/charts")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"service": "visualization", "status": "running"}


from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="output"), name="static")
