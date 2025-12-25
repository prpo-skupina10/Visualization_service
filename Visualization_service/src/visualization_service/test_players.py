import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="player_service",
    user="postgres",
    password="Kobe,Bryant123"
)

df = pd.read_sql("SELECT * FROM players", conn)
conn.close()

print(df.head())
print(df.columns)
print("Rows:", len(df))
