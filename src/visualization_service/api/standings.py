from fastapi import APIRouter
from visualization_service.loaders import load_standings
from visualization_service.charts import standings_table


router = APIRouter(prefix="/standings", tags=["standings"])

@router.get("/{league_id}/{season}")
def standings_chart(league_id: int, season: int):
    df = load_standings(league_id, season)
    path = standings_table(df)
    return {
        "league_id": league_id,
        "season": season,
        "chart_url": f"/api/charts/static/{path.split('/')[-1]}"
    }