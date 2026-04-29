import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    return pd.read_csv("data/nsl_kdd.csv")

def preprocess(df):
    df = df.copy()

    # Convert labels: normal = 0, attack = 1
    df["label"] = df["label"].apply(
        lambda x: 0 if str(x).lower() == "normal" else 1
    )

    # Encode categorical columns
    cat_cols = ["protocol_type", "service", "flag"]

    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

    X = df.drop(columns=["label"])
    y = df["label"]

    return X, y