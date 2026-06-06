import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "employees.csv")


def save_employees_csv(data: dict) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False)


data = {
    "name": ["Alice", "Bob", "Charlie", "Sailesh", "Lukas"],
    "age": [25, 30, 22, 19, 24],
    "salary": [50000, 60000, 45000, 55000, 80000]
}

save_employees_csv(data)
print(f"CSV file saved successfully to {OUTPUT_FILE}!")
