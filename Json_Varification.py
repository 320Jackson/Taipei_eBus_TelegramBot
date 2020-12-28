import os
import json

with open('./StopInfo/TPE_Stop.json', 'r') as f:
    JsonObj = json.loads(f.read())

for Run in JsonObj:
    print(Run['StopID'])