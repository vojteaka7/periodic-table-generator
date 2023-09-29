import json

with open('pertab_with_ox_states.json', encoding='utf-8') as f:
    pertab_oxidy = json.load(f)

with open('pertab.json', encoding='utf-8') as f:
    pertab_bez = json.load(f)['elements']


for prvek in pertab_oxidy:
    cislo = prvek['atomicNumber']
    
    for i, prvek_bez in enumerate(pertab_bez):
        if prvek_bez['number'] == cislo:
            pertab_bez[i]['oxidation_states'] = prvek['oxidationStates'] if prvek['oxidationStates'] != 'unknown' else ''


with open('pertab_oxidation_states.json', 'w', encoding='utf-8') as f:
    output = json.dumps({'elements': pertab_bez}, indent=4)
    f.write(output)
