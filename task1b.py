import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
dis_data = pd.read_csv("Trips_by_Distance.csv")
full_data = pd.read_csv("Trips_Full Data.csv")

# Fill NaN values and drop remaining NaNs
#dis_data = dis_data.fillna(dis_data.mean(numeric_only=True)).dropna()

# Filter data for trips greater than 10 million
for_10_25 = dis_data[dis_data['Number of Trips 10-25'] > 10000000]
for_50_100 = dis_data[dis_data['Number of Trips 50-100'] > 10000000]

# Plot the scatter plots
print(f"There are {len(for_10_25)} dates with >10M trips in the 10-25 miles category")
print(f"There are {len(for_50_100)} dates with >10M trips in the 50-100 miles category")


