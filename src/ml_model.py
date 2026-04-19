from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
import pandas as pd

def prepare_features(df):
    df = df.copy()
    df = pd.get_dummies(df, columns=['category'], drop_first=True)
    return df

def train_model(df):
    df = prepare_features(df)

    X = df.drop(columns=['amount','date','payment_method'])
    y = df['amount']

    model = LinearRegression()
    model.fit(X,y)

    return model, X.columns

def predict(model, cols, df):
    df = prepare_features(df)

    for col in cols:
        if col not in df.columns:
            df[col] = 0

    df = df[cols]
    return model.predict(df)

def detect_anomaly(df):
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[['amount']])
    return df[df['anomaly'] == -1]