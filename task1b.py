import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
dis_data = pd.read_csv("trips_by_distance.csv")
full_data = pd.read_csv("trips_full_data.csv")

# Fill NaN values and drop remaining NaNs
dis_data = dis_data.fillna(dis_data.mean(numeric_only=True)).dropna()

# Filter data for trips greater than 10 million
for_10_25 = dis_data[dis_data['Number of Trips 10-25'] > 10000000]
for_50_100 = dis_data[dis_data['Number of Trips 50-100'] > 10000000]

# Plot the scatter plots
plt.figure(figsize=(10, 6))

# Plot the first scatter plot
plt.scatter(for_50_100['Date'], for_50_100['Number of Trips 50-100'], color='blue', label='Trips 50-100')

# Plot the second scatter plot
plt.scatter(for_10_25['Date'], for_10_25['Number of Trips 10-25'], color='green', label='Trips 10-25')

# Add labels and title
plt.xlabel('Dates')
plt.ylabel('Number of Trips')
plt.title('Overlapping Scatter Plot: Trips 10–25 vs 50–100')
plt.grid(True)
plt.legend()

# Save the plot
plt.savefig("scatterplot.png")

# Show the plot
plt.show()


