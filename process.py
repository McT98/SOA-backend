import json
import os

file_dir = './data'
files = os.listdir(file_dir)

dic = {}
i = 0
while i < len(files):
    date = files[i][5:10]
    while i < len(files) and date == files[i][5:10]:
        i += 1
    file = files[i-1]
    print(file)
    with open(file_dir+'/'+file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    stats = ['currentConfirmedCount', 'confirmedCount', 'suspectedCount', 'curedCount', 'deadCount']
    for area in data['results']:
        countryName = ''
        if 'countryName' in area:
            countryName = area['countryName']
        else:
            countryName = area['country']
        name = countryName
        if countryName != area['provinceName']:
            name = countryName + area['provinceName']
        if not name in dic:
            dic[name] = {'cities':[], 'date':[]}
        dic[name]['date'].append(date)
        if 'locationId' in area and not 'locationId' in dic[name]:
            dic[name]['locationId'] = area['locationId']
        dic[name][date] = {}
        for stat in stats:
            if stat in area:
                dic[name][date][stat] = area[stat]
        if area['cities'] == None:
            continue
        for city in area['cities']:
            cityName = city['cityName']
            if not cityName in dic[name]['cities']:
                dic[name]['cities'].append(cityName)
                dic[name][cityName] = {}
            dic[name][cityName][date] = {}
            for stat in stats:
                if stat in city:
                    dic[name][cityName][date][stat] = city[stat]

s = json.dumps(dic, ensure_ascii=False)
with open('./data.json', 'w', encoding='utf-8') as f:
    f.write(s)