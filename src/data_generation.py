import pandas as pd
import numpy as np
import os

def generate_data(n=500):
    np.random.seed(42)
    os.makedirs("data", exist_ok=True)

    dates = pd.date_range("2024-01-01", "2024-12-31")
    categories = ["Food", "Travel", "Rent", "Shopping", "Bills", "Entertainment"]

    df = pd.DataFrame({
        "date": np.random.choice(dates, n),
        "category": np.random.choice(categories, n),
        "amount": np.random.randint(100, 5000, n),
        "payment_method": np.random.choice(["Cash","Card","UPI"], n)
    })

    return df