import pandas as pd
import numpy as np

# Load real traffic dataset (adjust path to your file)
df = pd.read_csv('c:/Users/hp/OneDrive/Desktop/Gsoc-prep/Data preprosesing/traffic.csv')  # Your file path

# Preview the raw data
print("Raw Data Preview:\n", df.head())

# Step 1: Handle missing values by filling with the mean of 'Vehicles'
mean_volume = df['Vehicles'].mean()  # Updated column name
df['Vehicles'].fillna(mean_volume, inplace=True)
print("\nAfter filling missing values:\n", df.head())

# Step 2: Cap outliers (e.g., cap Vehicles at 5000 as an unrealistic spike)
cap_threshold = 5000
df['Vehicles'] = df['Vehicles'].apply(lambda x: min(x, cap_threshold))
print("\nAfter capping outliers at 5000:\n", df.head())

# Step 3: Save to structured formats
df.to_csv('processed_traffic.csv', index=False)
df.to_parquet('processed_traffic.parquet')
print("\nData saved as CSV and Parquet!")

# Verify saved files
print("\nCSV file head:\n", pd.read_csv('processed_traffic.csv').head())
print("\nParquet file head:\n", pd.read_parquet('processed_traffic.parquet').head())