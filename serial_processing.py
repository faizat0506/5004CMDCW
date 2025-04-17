import pandas as pd
import time

# Load data
data = pd.read_csv('trips_by_distance.csv')

# Start timer
start_time = time.time()

# Data processing logic
result = data.groupby('population Not Staying at Home').sum()

# End timer
end_time = time.time()
execution_time_serial = end_time - start_time

print(f"Serial Processing Time: {execution_time_serial} seconds")
