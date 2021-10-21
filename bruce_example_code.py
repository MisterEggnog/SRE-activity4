import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

logfilename = 'nasa_access_log_500k.csv'

print(f"reading file: {logfilename}")
df = pd.read_csv(logfilename, low_memory=False, parse_dates=['timestamp'])

# Question 1. What is the date range for this access log?

print("\nQuestion 1:\n\tcalculate date range")
mindate = min(df['timestamp']).date()
maxdate = max(df['timestamp']).date()
print (f"\tdate range: {mindate} to {maxdate}")

# Question 2. Display a pie chart of in which each pie slice 
# represents a response code and the size of the pie piece is 
# proportional to the number of responses with that code.

print("\nQuestion 2: response code pie chart")
vc = df['rcode'].value_counts()
print(f"\nValue Counts for 'rcode':\n{vc}")
vc.plot.pie(figsize=(10,10))
plt.show()

# Question 3. How many different, unique clients access the service.
# Verified using
#   tail -n +2 < nasa_access_log_500k.csv | awk -F, '{ print $2 }' | sort -u | wc -l
print('\nQuestion 3: Unique clients')
uniq = df['clientloc'].nunique()
print(f"\nSite recieved {uniq} visitors\n")

print('\nQuestion 4: Which Client Accessed The Most')
mostCommonClient = df['clientloc'].value_counts()
print(f"\nThe most common client was {mostCommonClient.index[0]}, they connected {mostCommonClient[0]} times\n")

print("Done")

