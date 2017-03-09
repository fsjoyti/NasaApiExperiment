import requests
import json
user_query = raw_input()
api_key = '8hv4srmf33gIQNsjPlPBYkgxIp2wyf2Ncx1cr2nq'
payload = {'query': user_query , 'limit': 20, 'api_key':api_key}
response = requests.get('https://api.nasa.gov/patents/content',params=payload)
output = set()
data = response.json()
for result in data['results']:
    email = result['contact']['email']
    output.add(str(email))
mynewlist = list(output)
for x in sorted(mynewlist,key=str.lower):
    print x
