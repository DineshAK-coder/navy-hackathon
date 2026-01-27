import pandas as pd
import numpy as np
import datetime

# Create 1,000 data points representing daily logs
np.random.seed(42)
days = 1000
date_rng = pd.date_range(start='2024-01-01', periods=days, freq='D')

# Variables
torque = np.random.uniform(70, 95, size=days)  # Engine power %
water_temp = np.random.uniform(15, 30, size=days) # Warmer water = faster growth
days_since_clean = np.arange(days) % 200 # Resets every 200 days (simulated cleaning)

# Physics Logic: Speed = (Torque * Constant) - (Drag from Fouling)
# Drag increases based on days_since_clean and water_temp
fouling_drag = (days_since_clean ** 1.5) * (water_temp / 1000)
speed = (torque * 0.25) - fouling_drag + np.random.normal(0, 0.1, size=days)

df = pd.DataFrame({
    'date': date_rng,
    'torque_pct': torque,
    'water_temp_c': water_temp,
    'days_since_clean': days_since_clean,
    'actual_speed_knots': speed
})

df.to_csv('ship_performance.csv', index=False)
print("Dataset 'ship_performance.csv' created successfully!")