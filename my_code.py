import pandas as pd

# Create dataset
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 22, 28],
    "salary": [50000, 60000, 45000, 55000]
}


df = pd.DataFrame(data)


df.to_csv("employees.csv", index=False)

print("CSV file saved successfully!")
