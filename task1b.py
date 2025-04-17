import pandas as pd

dis_data = pd.read_csv("trips_by_distance.csv")

full_data = pd.read_csv("trips_full_data.csv")

dis_data = dis_data.fillna(dis_data.mean(numeric_only= True)).dropna()

for_10_25 = dis_data[dis_data['Number of Trips 10-25'] > 10000000]

for_50_100 = dis_data[dis_data['Number of Trips 50-100'] > 10000000]

import matplotlib.pyplot as plt

# Plot the first scatter plot
plt.scatter(for_50_100['Date'], for_50_100['Number of Trips 50-100'], color='blue')

# Plot the second scatter plot 
plt.scatter(for_10_25['Date'], for_10_25['Number of Trips 10-25'], color='green')

plt.xlabel('Dates')
plt.ylabel('Numbers of trip ')
plt.title('Overlapping Scatter Plot: Trips 10–25 vs 50–100')
plt.grid(True)
plt.savefig("scatterplot.png")
