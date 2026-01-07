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

import os
import pandas as pd

def standings_table(df: pd.DataFrame) -> str:
    """
    Generates a standings table image and saves it to output/.
    Returns relative path to the image.
    """

    # --- basic cleanup ---
    df = df.sort_values("position").reset_index(drop=True)
    df["GD"] = df["goals_for"] - df["goals_against"]

    display_df = df[[
        "position",
        "team_name",
        "played",
        "wins",
        "draws",
        "losses",
        "goals_for",
        "goals_against",
        "GD",
        "points"
    ]]

    display_df.columns = [
        "#", "Team", "P", "W", "D", "L", "GF", "GA", "GD", "Pts"
    ]

    # --- figure ---
    fig, ax = plt.subplots(figsize=(12, 0.5 * len(display_df) + 1))
    ax.axis("off")

    table = ax.table(
        cellText=display_df.values,
        colLabels=display_df.columns,
        loc="center",
        cellLoc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.4)

    # --- header styling ---
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#222222")
            cell.set_text_props(color="white", weight="bold")

    # --- row coloring ---
    n = len(display_df)

    for i in range(1, n + 1):
        if i == 1:  # champion
            color = "#d4af37"  # gold
        elif i > n - 3:  # relegation
            color = "#f4cccc"  # light red
        else:
            color = "#ffffff"

        for j in range(len(display_df.columns)):
            table[(i, j)].set_facecolor(color)

    # --- save ---
    os.makedirs("output", exist_ok=True)
    path = "output/standings.png"
    plt.savefig(path, bbox_inches="tight")
    plt.close()

    return path


