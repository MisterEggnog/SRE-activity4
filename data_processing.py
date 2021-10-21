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
def mostCommonElem(frame, axis):
    return frame[axis].value_counts()
mostCommonClient = mostCommonElem(df, 'clientloc')
print(f"\nThe most common client was {mostCommonClient.index[0]}, they connected {mostCommonClient[0]} times\n")

print('\nQuestion 5: For the 5 clients with the most requests, show a bar chart of how many times each client accessed the service.')
mostCommonClientBar = mostCommonClient.iloc[0:5]
mostCommonClientBar.plot.bar(figsize=[10,10])
plt.show()
print(f"\n{mostCommonClientBar}")

print('\nQuestion 6: Which resource (which path) was accessed the most?')
mostCommonResource = mostCommonElem(df, 'path')
print(f'\nMost commonly accessed resource was {mostCommonResource.index[0]}')

print('\nQuestion 7: The first element in the path indicates a resource class. List all of the accessed resource classes.')
mostCommonResourceClass = df['path'].map(lambda a : a.split('/')[1]).value_counts()
print(f'\n{mostCommonResourceClass.index.tolist()}\n')

print("Done")

