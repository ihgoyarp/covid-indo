import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

response_API = requests.get('https://data.covid19.go.id/public/api/update.json')
data = response_API.text

data = json.loads(data)
dates = [i['key_as_string'] for i in data['update']['harian']]
values = [i['jumlah_positif']['value'] for i in data['update']['harian']]

df = pd.DataFrame({'dates': dates, 'values': values})
df['dates'] = [pd.to_datetime(i) for i in df['dates']]

#print(df.sort_values(by='dates'))
plt.plot(dates, values)
plt.show()
