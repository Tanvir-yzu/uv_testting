# main.py
import pandas as pd

# 1️⃣ Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2️⃣ Save DataFrame to CSV
df.to_csv("people.csv", index=False)
print("\nSaved to people.csv")

# 3️⃣ Read DataFrame from CSV
df2 = pd.read_csv("people.csv")
print("\nRead from CSV:")
print(df2)

# 4️⃣ Basic operations
print("\nAverage Age:", df["Age"].mean())
print("Max Age:", df["Age"].max())
print("Min Age:", df["Age"].min())

# 5️⃣ Filtering rows
older_than_30 = df[df["Age"] > 30]
print("\nPeople older than 30:")
print(older_than_30)

# 6️⃣ Adding a new column
df["Age in 5 years"] = df["Age"] + 5
print("\nDataFrame with new column:")
print(df)
