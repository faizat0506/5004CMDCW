import dask
# Disable the new arrow-based string conversion in Dask
dask.config.set({"dataframe.convert-string": False})

import time
import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt

# Simulated "processor" list for demonstration;
# .compute() won't actually vary the number of workers with these.
n_processors = [10, 20]
n_processors_time = {}


# Read CSV entirely with Pandas (bypassing Dask's CSV parser)


pdf = pd.read_csv("Trips_by_Distance.csv")

#  Convert columns to avoid Arrow-based dtypes

pdf["Number of Trips 10-25"] = pd.to_numeric(pdf["Number of Trips 10-25"], errors="coerce")
pdf["Number of Trips 50-100"] = pd.to_numeric(pdf["Number of Trips 50-100"], errors="coerce")

#  Create a Dask DataFrame from the in-memory Pandas DataFrame

dask_df = dd.from_pandas(pdf, npartitions=4)

# Parallel filtering and timing demonstration

for processor in n_processors:
    print(f"\n(Simulating) Processing with {processor} processor=")
    start_time = time.time()

    #  Filter "Number of Trips 10-25" > 10 million
    trips_10_25 = dask_df[dask_df["Number of Trips 10-25"] > 1e7][["Date", "Number of Trips 10-25"]]
    trips_10_25 = trips_10_25.compute()

    # Filter "Number of Trips 50-100" > 10 million
    trips_50_100 = dask_df[dask_df["Number of Trips 50-100"] > 1e7][["Date", "Number of Trips 50-100"]]
    trips_50_100 = trips_50_100.compute()

    # Record time
    dask_time = time.time() - start_time
    n_processors_time[processor] = dask_time

    # Print results
    print(f"10-25 Trips (>10M): {len(trips_10_25)} rows")
    print(f"50-100 Trips (>10M): {len(trips_50_100)} rows")
    print(f"Time taken: {dask_time:.2f} seconds")


#  Summary

print("\nSummary of times by (intended) number of processors ")
for proc, t in n_processors_time.items():
    print(f"{proc} processors: {t:.2f} seconds")
