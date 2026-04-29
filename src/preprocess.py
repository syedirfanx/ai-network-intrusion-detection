import pandas as pd

def load_data():
    return pd.read_csv("data/nsl_kdd.csv")

def preprocess(df):
    df = df.copy()

    # Convert labels: normal = 0, attack = 1
    df["label"] = df["label"].apply(
        lambda x: 0 if str(x).lower() == "normal" else 1
    )

    X = df.drop(columns=["label"])
    y = df["label"]

    return X, y