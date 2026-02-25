import requests
from datetime import datetime, timedelta

today=datetime.now()
week_ago=today-timedelta(days=7)

#turning into string
start_date=week_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")


#API URL
url=f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response=requests.get(url)
data=response.json()


#To display in Tabular data
import pandas as pd

req=data['daily']

df={'date':req['time'],'max_temp':req['temperature_2m_max'],'min_temp':req['temperature_2m_min']}
dataframe=pd.DataFrame(df)
print(dataframe)


import matplotlib.pyplot as plt

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dataframe['date'], dataframe['max_temp'], marker='o', label='Max Temp')
plt.plot(dataframe['date'], dataframe['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()
