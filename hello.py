import matplotlib.pyplot as plt
import requests
import json
response_API = requests.get(
    'https://data.covid19.go.id/public/api/update.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
# counter = 0

# x axis values
# x = parse_json['update']['harian'][2]['jumlah_positif']['value']
# for jumlah in parse_json['update']['harian']:
#     counter += 1
#     x = jumlah['jumlah_positif']['value']

# for tgl in parse_json['update']['harian']:
#     counter += 1
#     y = tgl['key_as_string']

xAxis = [key for key, value in parse_json.items(['update']['harian']['jumlah_positif']['value'])]
yAxis = [value for key, value in parse_json['update']['harian']['key_as_string']]
plt.grid(True)

## LINE GRAPH ##
plt.plot(xAxis, yAxis, color='maroon', marker='o')
plt.xlabel('variable')
plt.ylabel('value')

# print(x)

# plt.plot(x, y)

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')

# plt.title('My first graph!')

plt.show()
