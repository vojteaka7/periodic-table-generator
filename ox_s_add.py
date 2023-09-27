def compress_oxidation_states(txt):
    if txt == '':
        return txt
    
    def find_max(i, l):
        if i +1 == len(l):
            return i
        
        if l[i]+1 == l[i+1]:
            return find_max(i+1, l)
        else:
            return i
    
    ox_s = txt.split(', ')
    ox_s = [int(x) for x in ox_s]

    output = []
    
    i = 0
    while i < len(ox_s):
        s = i
        c = find_max(i, ox_s)

        if s == c:
            output.append(str(ox_s[s]))
            i += 1
        elif ox_s[s]+1 == ox_s[c]:
            output.append(str(ox_s[s]))
            output.append(str(ox_s[c]))
            i = c+1
        else:
            output.append(f"{ox_s[s]}...{ox_s[c]}")
            i = c + 1

    return ', '.join(output)

import json

with open('pertab_oxidy.json', encoding='utf-8') as f:
    pertab = json.load(f)['elements']


for i, prvek in enumerate(pertab):
    pertab[i]['ox_s'] = compress_oxidation_states(str(prvek['oxidation_states']))
 
with open('pertab_ox_s.json', 'w', encoding='utf-8') as f:
    output = json.dumps({'elements': pertab}, indent=4)
    f.write(output)
