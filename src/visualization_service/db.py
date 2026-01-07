import psycopg2
import os

def get_connection_to_players():
    return psycopg2.connect(
        host=os.getenv("PLAYER_DB_HOST"),
        port=5432,
        dbname=os.getenv("PLAYER_DB_NAME"),
        user=os.getenv("PLAYER_DB_USER"),
        password=os.getenv("PLAYER_DB_PASSWORD"),
    )

def get_connection_to_teams():
    return psycopg2.connect(
        host=os.getenv("TEAM_DB_HOST"),
        port=5432,
        dbname=os.getenv("TEAM_DB_NAME"),
        user=os.getenv("TEAM_DB_USER"),
        password=os.getenv("TEAM_DB_PASSWORD"),
    )

def get_connection_to_leagues():
    return psycopg2.connect(
        host=os.getenv("LEAGUE_DB_HOST"),
        port=5432,
        dbname=os.getenv("LEAGUE_DB_NAME"),
        user=os.getenv("LEAGUE_DB_USER"),
        password=os.getenv("LEAGUE_DB_PASSWORD"),
    )

def close_connection(conn):
    return conn.close

