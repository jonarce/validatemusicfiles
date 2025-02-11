import json
m = {'id': 2, 'name': 'hussain'}
n = json.dumps(m)
o = json.loads(n)
print(o['id'], o['name'])

