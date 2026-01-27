from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
# Load data
data = pd.read_csv('ship_performance.csv')

# Feature selection: We train ONLY on clean data (first 30 days after cleaning)
clean_data = data[data['days_since_clean'] < 30]
X = clean_data[['torque_pct', 'water_temp_c']]
y = clean_data['actual_speed_knots']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# Prediction: Calculate "Predicted Speed" for the whole dataset
# ... (after your model.fit code) ...

# 1. Generate predictions for the entire dataset
data['predicted_speed'] = model.predict(data[['torque_pct', 'water_temp_c']])

# 2. Calculate Efficiency Loss (The missing part!)
# Logic: (Predicted Speed - Actual Speed) / Predicted Speed * 100
data['efficiency_loss'] = ((data['predicted_speed'] - data['actual_speed_knots']) / data['predicted_speed']) * 100

# 3. Clean up: Ensure no negative loss (if actual speed is slightly higher than predicted)
data['efficiency_loss'] = data['efficiency_loss'].clip(lower=0)

# 4. Save it
data.to_csv('processed_results.csv', index=False)
print("Success: 'processed_results.csv' now contains the efficiency_loss column.")