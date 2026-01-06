import pandas as pd
import matplotlib as plt
from visualization_service.charts import players_by_position
from visualization_service.loaders import load_players_by_team_id

df_mu = load_players_by_team_id(33)
graph = players_by_position(df_mu)

print(df_mu.shape)
print(graph)