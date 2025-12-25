from visualization_service.loaders import load_teams_by_league_id, load_players_by_team_ids

teams_df = load_teams_by_league_id(39)

team_ids = teams_df["api_id"].tolist()
print("Teams:", team_ids)


players_df = load_players_by_team_ids(team_ids)

print("Players loaded:", len(players_df))
#print(players_df.head(6))

df = players_df.merge(
    teams_df[["api_id", "name"]],
    left_on="team_id",
    right_on="api_id",
    how="inner"
)
print(df.groupby("team_id").size().sort_values())
df = df[df["age"] <= 50]
df = df.rename(columns={"name_y":"Team name"})
#print(df.head(5))

avg_age = (
    df.dropna(subset=["age"])
      .groupby("Team name")["age"]
      .mean()
      .sort_values(ascending=False)
)

#print(avg_age.head(5))

import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)

plt.figure(figsize=(12, 6))
avg_age.plot(kind="bar")
plt.ylabel("Average age")
plt.title("Average age per team – Premier League")
plt.tight_layout()
plt.savefig("output/avg_age_per_team.png")
plt.close()


