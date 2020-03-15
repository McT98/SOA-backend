import json
with open('./urls.json', 'r') as f:
    urls = json.load(f)
print(len(urls))