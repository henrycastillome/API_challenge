import json
import requests
import re 



api=f"https://data.cityofnewyork.us/resource/uip8-fykc.json"
r=requests.get(url=api)

data_json=r.json()

data_str=json.dumps(data_json, indent=2) 

match=re.search(r'HISPANIC+', data_str)

if match:
    print('found', match.group())
else:
    print('did not find')

