import pandas as pd
import matplotlib.pyplot as plt

dis_data = pd.read_csv("trips_by_distance.csv")

full_data = pd.read_csv("trips_full_data.csv")

dis_data = dis_data.fillna(dis_data.mean(numeric_only= True)).dropna()

plt.figure(figsize=(12, 6))
total_trips.plot(kind='bar', color='darkred')
plt.title('Trip Distribution by Distance')
plt.xlabel('Distance Range (miles)')
plt.ylabel('Number of Trips')
plt.xticks(ticks=range(len(distance_column)), labels=distance_column, rotation=45)
plt.tight_layout()
plt.savefig("trip_distance_distribution.png")
