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


'Level', 'Date', 'State FIPS', 'State Postal Code', 'County FIPS',
       'County Name', 'Population Staying at Home',
       'Population Not Staying at Home', 'Number of Trips',
       'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5',
       'Number of Trips 5-10', 'Number of Trips 10-25',
       'Number of Trips 25-50', 'Number of Trips 50-100',
       'Number of Trips 100-250', 'Number of Trips 250-500',
       'Number of Trips >=500', 'Row ID', 'Week', 'Month'],
      dtype='object'
