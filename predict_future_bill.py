import pickle
import pandas as pd

# Load ML model
with open("bill_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Household Selection
print("AVAILABLE HOUSEHOLDS")

houses = [
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

for i, house in enumerate(houses, start=1):
    print(f"{i}. {house}")

choice = int(input("\nSelect House: "))
selected_house = houses[choice - 1]

print(f"\nSelected Household: {selected_house}")

print("\nAI ELECTRICITY BILL FORECASTING SYSTEM")
print("=" * 50)

# Power Inputs
print("\nEnter Appliance Power Ratings (Watts)")

ac_power = float(input("Air Conditioner: "))
fridge_power = float(input("Refrigerator: "))
tv_power = float(input("Television: "))
wm_power = float(input("Washing Machine: "))
motor_power = float(input("Water Motor: "))
induction_power = float(input("Induction Stove: "))
fan_power = float(input("Ceiling Fans: "))
light_power = float(input("Lighting: "))
charger_power = float(input("Mobile Chargers: "))

# Hours Inputs
print("\nEnter Hours Used Per Day")

ac_hours = float(input("AC Hours/Day: "))
fridge_hours = float(input("Refrigerator Hours/Day: "))
tv_hours = float(input("TV Hours/Day: "))
wm_hours = float(input("Washing Machine Hours/Day: "))
motor_hours = float(input("Water Motor Hours/Day: "))
induction_hours = float(input("Induction Stove Hours/Day: "))
fan_hours = float(input("Fans Hours/Day: "))
light_hours = float(input("Lights Hours/Day: "))
charger_hours = float(input("Chargers Hours/Day: "))

# Monthly Units Calculation
ac_units = (ac_power * ac_hours * 30) / 1000
fridge_units = (fridge_power * fridge_hours * 30) / 1000
tv_units = (tv_power * tv_hours * 30) / 1000
wm_units = (wm_power * wm_hours * 30) / 1000
motor_units = (motor_power * motor_hours * 30) / 1000
induction_units = (induction_power * induction_hours * 30) / 1000
fan_units = (fan_power * fan_hours * 30) / 1000
light_units = (light_power * light_hours * 30) / 1000
charger_units = (charger_power * charger_hours * 30) / 1000

# Scale values to training range
scale_factor = 100000

data = pd.DataFrame(
    [[
        ac_units * scale_factor,
        fridge_units * scale_factor,
        tv_units * scale_factor,
        wm_units * scale_factor,
        motor_units * scale_factor,
        induction_units * scale_factor,
        fan_units * scale_factor,
        light_units * scale_factor,
        charger_units * scale_factor
    ]],
    columns=[
        "Appliance1",
        "Appliance2",
        "Appliance3",
        "Appliance4",
        "Appliance5",
        "Appliance6",
        "Appliance7",
        "Appliance8",
        "Appliance9"
    ]
)

# Predict Bill
predicted_bill = model.predict(data)[0]

# Appliance Analysis
appliances = {
    "Air Conditioner": ac_units,
    "Refrigerator": fridge_units,
    "Television": tv_units,
    "Washing Machine": wm_units,
    "Water Motor": motor_units,
    "Induction Stove": induction_units,
    "Ceiling Fans": fan_units,
    "Lighting": light_units,
    "Mobile Chargers": charger_units
}

total_units = sum(appliances.values())

highest = max(appliances, key=appliances.get)
highest_units = appliances[highest]
highest_percentage = (highest_units / total_units) * 100

print("\nMONTHLY ENERGY ANALYSIS")
print("=" * 50)

for appliance, units in appliances.items():

    percentage = (units / total_units) * 100 if total_units > 0 else 0

    print(
        f"{appliance:<20} "
        f"{units:>8.2f} kWh "
        f"({percentage:.1f}%)"
    )

print("\nRESULTS")
print("=" * 50)

print(f"Selected Household       : {selected_house}")
print(f"Predicted Next Month Bill: ₹{predicted_bill:.2f}")
print(f"Estimated Monthly Units  : {total_units:.2f} kWh")
print(f"Highest Consumer         : {highest}")
print(f"Contribution Percentage  : {highest_percentage:.1f}%")