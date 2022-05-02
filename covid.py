import requests
import json
response_API = requests.get(
    'https://data.covid19.go.id/public/api/update.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)

active_case = parse_json['update']['harian']
print(json.dumps(parse_json, indent=4))
