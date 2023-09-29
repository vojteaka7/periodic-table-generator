# Periodic table generator

You can use the pregenerated periodic table (`pertab.html`) or edit the `templates/element.html` jinja2 template.

## Dependencies 

The only dependency is Jinja2. You can install it with pip:

```shell
pip instal jinja2
```

## Elements data

The data about elements was taken from [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON). I added oxidation states data from the `pertab_with_ox_states.json` copied from <https://documenter.getpostman.com/view/14793990/TzmCgD9k#618ced08-5d55-49ea-8638-9393daf30daa> (the actual API doesn't work). Czech names were added manually. 

---

# Generátor periodické tabulky

Můžete použít předgenerovanou tabulku (`pertab.html`) nebo upravit Jinja2 šablonu v souboru `templates/element.html`.

## Závislosti

Jedinou závislostí je Jinja2. Lze nainstalovat pomocí pip:

```shell
pip install jinja2
```

## Data o prvcích

Data o prvcích byla získána z [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON). Též jsem přidal oxidační čísla ze souboru `pertab_with_ox_states.json`, který byl získán z <https://documenter.getpostman.com/view/14793990/TzmCgD9k#618ced08-5d55-49ea-8638-9393daf30daa> (touto stánkou popisované API veskutečnosti nefunguje). České názvy byly přidány manuálně.
