import requests
import duckdb
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

url = 'https://api.exchangerate.host/timeseries?start_date=2022-01-01&end_date=2023-01-04&symbols=CZK,USD,SA,EUR,CAD&places=2'
response = requests.get(url)
data = response.json()

with open("data.json" , "w") as f:
    json.dump(data , f)



date_of_ratee = list(data['rates'].keys())


#print(date_of_ratee)

date_and_rate = []
for one_date in date_of_ratee:
    rate_by_date = data['rates'][one_date]['CZK']
    date_and_rate.append((one_date, rate_by_date))



# Extract the x and y data
x_data = [d[0] for d in date_and_rate] 

y_data = [d[1] for d in date_and_rate]

# Plot the data
fig, ax = plt.subplots()
ax.plot(x_data, y_data)

# Format the x-axis tick labels
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Rotate the x-axis tick labels if needed
fig.autofmt_xdate(rotation=45)

# Plot the data
#plt.plot(x_data, y_data)

# Add labels to the plot
plt.xlabel('Date')
plt.ylabel('CZK rates')
plt.title('Data Plot')

# Display the plot
plt.show()
