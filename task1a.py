import pandas as pd

dis_data = pd.read_csv("trips_by_distance.csv")

full_data = pd.read_csv("trips_full_data.csv")

dis_data = dis_data.fillna(dis_data.mean(numeric_only= True)).dropna()

home_week_average = dis_data.groupby('Week')['Population Staying at Home'].mean().reset_index()

travel_week_average = dis_data.groupby('Week')[['Number of Trips <1','Number of Trips >=500']].mean()

distance_column=[
'Number of Trips <1',                
'Number of Trips 1-3',               
'Number of Trips 3-5',              
'Number of Trips 5-10',              
'Number of Trips 10-25',             
'Number of Trips 25-50',             
'Number of Trips 50-100',            
'Number of Trips 100-250',           
'Number of Trips 250-500',           
'Number of Trips >=500' 
]
# calculate total trips per grouped mile 
total_trips = dis_data[distance_column].sum()

# define midpoint distances for each grouped mile
midpoints = [0.5, 2, 4, 7.5, 17.5, 37.5, 75, 175, 375, 500]

# calculate weighted average distance
weighted_avg_distance = (total_trips * midpoints).sum() / total_trips.sum()

print ( "Average population at home per week:",home_week_average)
print ("Average population traveling per week",weighted_avg_distance)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(home_week_average['Week'], home_week_average['Population Staying at Home'], color='blue', linestyle= '-')
plt.title('Average Weekly Population Staying at Home')
plt.xlabel('Week')
plt.ylabel('Number of People')
plt.grid(True)

plt.savefig("weekly_home_avg.png")

