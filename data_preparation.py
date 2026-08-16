import pandas as pd

files = [
    "House_1.csv",
    "House_2.csv",
    "House_3.csv",
    "House_4.csv",
    "House_5.csv",
    "House_6.csv",
    "House_7.csv",
    "House_8.csv",
    "House_9.csv",
    "House_10.csv",
    "House_11.csv",
    "House_12.csv",
    "House_13.csv",
    "House_15.csv",
    "House_16.csv",
    "House_17.csv",
    "House_18.csv",
    "House_19.csv",
    "House_20.csv",
    "House_21.csv"
]

all_data = []

for file in files:

    print(f"Reading {file}")

    df = pd.read_csv(file, nrows=1000000)

    df["House"] = file

    all_data.append(df)

combined = pd.concat(all_data, ignore_index=True)

combined.to_csv(
    "combined_refit.csv",
    index=False
)

print("\nDataset Created Successfully")
print(combined.shape)

import pandas as pd

print("Loading combined dataset...")

df = pd.read_csv("combined_refit.csv")

print("Converting date column...")

df["Time"] = pd.to_datetime(df["Time"])

df["Month"] = df["Time"].dt.to_period("M")

monthly = df.groupby(
    ["House", "Month"]
).agg({
    "Appliance1": "sum",
    "Appliance2": "sum",
    "Appliance3": "sum",
    "Appliance4": "sum",
    "Appliance5": "sum",
    "Appliance6": "sum",
    "Appliance7": "sum",
    "Appliance8": "sum",
    "Appliance9": "sum",
    "Aggregate": "sum"
}).reset_index()

monthly.to_csv(
    "monthly_energy_dataset.csv",
    index=False
)

print("\nMonthly dataset created successfully!")
print(monthly.shape)

print("\nFirst few rows:")
print(monthly.head())

import pandas as pd

df = pd.read_csv("monthly_energy_dataset.csv")

# Convert Aggregate to approximate units
df["Units"] = df["Aggregate"] / 1000000

def calculate_bill(units):

    if units <= 100:
        return units * 3

    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)

    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 8)

df["Bill"] = df["Units"].apply(calculate_bill)

df.to_csv("bill_dataset.csv", index=False)

print(df[["House", "Month", "Units", "Bill"]].head())

print("\nDataset Shape:")
print(df.shape)