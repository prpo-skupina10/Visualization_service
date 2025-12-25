import psycopg2

def get_connection_to_players():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="player_service",
        user="postgres",
        password="Kobe,Bryant123"
    )

def get_connection_to_teams():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="team_service",
        user="postgres",
        password="Kobe,Bryant123"
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

