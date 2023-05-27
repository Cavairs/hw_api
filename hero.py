import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)
with open('hero.json', 'w', encoding='utf-8') as file:  
    json.dump(response.json(), file, ensure_ascii=False, indent=4)
    file.write('\n')    

with open('hero.json', 'r') as f_hero:
  data = json.load(f_hero)

intelligence_dict = {}

for id_item in data:
  if id_item['name'] in ['Hulk', 'Captain America', 'Thanos', 'A-bomb']:
    if 'intelligence' in id_item['powerstats']:
      intelligence_dict[id_item['name']] = id_item['powerstats']['intelligence']

max_intelligence = max(intelligence_dict.values())  #находим функцией max максимальное значение в словаре
for name, intelligence in intelligence_dict.items():
  print(f"{name} интелект {intelligence}.")
  if intelligence == max_intelligence:
    print()
    print(f"{name} является самым умным героем с интеллектом в {intelligence}.")






    