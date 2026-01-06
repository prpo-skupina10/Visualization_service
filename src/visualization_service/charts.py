import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def avg_age_per_team(players_df, teams_df):
    merged = players_df.merge(
        teams_df,
        left_on="team_id",
        right_on="api_id",
        suffixes=("_player", "_team")
    )

    avg_age = (
        merged
        .groupby("name_team")["age"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    avg_age.plot(kind="barh")
    plt.title("Average player age per team")
    plt.tight_layout()

    path = "output/avg_age_per_team.png"
    plt.savefig(path)
    plt.close()

    return path


def players_by_position(df):
    counts = df["position"].value_counts()

    plt.figure(figsize=(8,5))
    counts.plot(kind="bar")
    plt.title("Players by position")
    plt.tight_layout()

    path = "output/players_by_position.png"
    plt.savefig(path)
    plt.close()

    return path

