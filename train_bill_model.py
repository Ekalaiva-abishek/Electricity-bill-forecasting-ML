import pandas as pd
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

print("Loading dataset...")

df = pd.read_csv("bill_dataset.csv")

features = [
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

X = df[features]

y = df["Bill"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nModel Results")
print("=" * 40)

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

with open("bill_prediction_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel Saved Successfully")