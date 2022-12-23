
import requests


host = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
uri = '/all.json'
url = host + uri
response = requests.get(url)
info = response.json()
heroes_list = ['Hulk', 'Captain America', 'Thanos']

intelligence_dict = {}
for hero in info:
    if hero['name'] in heroes_list:
        intelligence_dict[hero['name']] = hero['powerstats']['intelligence']
print(intelligence_dict)
max_int = dict([max(intelligence_dict.items(), key=lambda k_v: k_v[1])])
print(f'Из трех супергероев, самый умный: {max_int}')