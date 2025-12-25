import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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

