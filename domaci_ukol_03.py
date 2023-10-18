import json

with open('body.json', 'r', encoding='utf-8') as soubor:
    data = json.load(soubor)

result = {}

for student, score in data.items():
    if score >= 60:
        result[student] = "Pass"
    else:
        result[student] = "Fail"

with open('prospech.json', 'w') as soubor:
    json.dump(result, soubor)