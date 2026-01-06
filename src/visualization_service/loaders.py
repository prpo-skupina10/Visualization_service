import pandas as pd
from visualization_service.db import get_connection_to_leagues, get_connection_to_players, get_connection_to_teams

def load_players()-> pd.DataFrame:
    with get_connection_to_players() as conn:
        return pd.read_sql("SELECT * FROM players", conn)

def load_teams()-> pd.DataFrame:
    with get_connection_to_teams() as conn:
        return pd.read_sql("SELECT * FROM teams", conn)

def load_team_ids_by_league(league_id: int) -> list[int]:
    with get_connection_to_teams() as conn:
        df = pd.read_sql("SELECT api_id FROM teams WHERE league_id = %s",conn,params=(league_id,))
    return df["api_id"].tolist()

def load_leagues()-> pd.DataFrame:
    with get_connection_to_leagues() as conn:
        return pd.read_sql("SELECT * FROM leagues", conn)
    
def load_players_by_team_id(team_id: int) -> pd.DataFrame:
    with get_connection_to_players() as conn:
        query = "SELECT * FROM players WHERE team_id = %s"
        return pd.read_sql(query, conn, params=(team_id,))
    
def load_teams_by_league_id(league_id: int) -> pd.DataFrame:
    with get_connection_to_teams() as conn:
        query = "SELECT * FROM teams WHERE league_id = %s"
        return pd.read_sql(query, conn, params=(league_id,))

def load_top_scorers(limit: int = 10) -> pd.DataFrame:
    with get_connection_to_players() as conn:
        query = "SELECT * FROM players ORDER BY goals DESC LIMIT %s"
        return pd.read_sql(query, conn, params=(limit,))
    
def load_player(player_id: int) -> pd.DataFrame:
    with get_connection_to_players() as conn:
        query = "SELECT * FROM players WHERE id = %s"
        return pd.read_sql(query, conn, params=(player_id,))

def load_players_by_team_ids(team_ids: list[int]) -> pd.DataFrame:
    if not team_ids:
        query = "SELECT * FROM players"
        with get_connection_to_players() as conn:
            return pd.read_sql(query, conn, params=team_ids)
    
    placeholders = ",".join(["%s"] * len(team_ids))

    query = f"""
    SELECT *
    FROM players
    WHERE team_id IN ({placeholders})
    """

    with get_connection_to_players() as conn:
        return pd.read_sql(query, conn, params=team_ids)

