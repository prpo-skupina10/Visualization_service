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
        host="localhost",
        port=5432,
        dbname="league_service",
        user="postgres",
        password="Kobe,Bryant123"
    )

def close_connection(conn):
    return conn.close

