import json

with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

keys = data.keys()
areas = []
for area in keys:
    areas.append(area)

s = json.dumps(areas, ensure_ascii=False)
with open('./areas.json', 'w', encoding='utf-8') as f:
    f.write(s)