import pandas as pd

# creating a DataFrame
data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
    ],
    "Age": [24, 27, 22, 32],
    "City": ["new York", "Los Angeles", "Chicago", "Houston"],
}
df = pd.DataFrame(data)

df = df.replace("Alice", "Alice Smith")
