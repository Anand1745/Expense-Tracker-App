from src.data_generation import generate_data

df = generate_data()
df.to_csv("data/expenses.csv", index=False)

print("Data Ready")