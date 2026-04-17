import pandas as pd

def transform():
    df = pd.read_csv("data.csv")
    df["total"] = df["price"] * df["quantity"]
    df.to_csv("output.csv", index=False)

if __name__ == "__main__":
    transform()