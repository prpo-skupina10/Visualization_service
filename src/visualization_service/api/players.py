from fastapi import APIRouter
from visualization_service.loaders import load_players_by_team_id
from visualization_service.charts import players_by_position

router = APIRouter(prefix="/players", tags=["players"])

@router.get("/{team_id}/by-position")
def players_by_position_chart(team_id: int):
    df = load_players_by_team_id(team_id)
    path = players_by_position(df)
    return {
        "team_id": team_id,
        "chart_url": f"/api/charts/static/{path.split('/')[-1]}"
    }
