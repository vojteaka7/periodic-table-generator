import json
from jinja2 import PackageLoader, select_autoescape
import jinja2

# Jinja2 setup
env = jinja2.Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)
prvek_template = env.get_template('element.html')
tabulka_template = env.get_template('table.html')


with open('pertab_ox_s.json', encoding='utf-8') as f:
    prvky = json.load(f)['elements']

tabulka = [['']*18 for _ in range(10+1)]

for p in prvky:
    p['atomic_mass'] = float(round(p['atomic_mass'], 0))

    
    tabulka[p['ypos']-1][p['xpos']-1] = prvek_template.render(p=p)
    

with open('pertab.html', 'w', encoding='utf-8') as f:
    output = tabulka_template.render(tabulka=tabulka)
    f.write(output)
