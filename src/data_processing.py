import pandas as pd

def load_data():
    df = pd.read_csv("data/expenses.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

def preprocess(df):
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df