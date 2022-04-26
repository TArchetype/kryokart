import json
import requests

webhook_url = 'http://127.0.0.1:8000/hook'

data = {
  "geometry": {
    "coordinates": [
    10.401731,
    63.418101
    ],
    "type": "Point"
  },
  "properties": {
    "name": "KryoKart"
  },
  "type": "Feature"
}

print(requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type' : 'application/json'}))