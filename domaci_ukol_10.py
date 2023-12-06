import pandas as pd

url_praha = "https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv"
url_plzen = "https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plze%C5%88.csv"
url_liberec = "https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv"

zam_praha = pd.read_csv(url_praha)
zam_plzen = pd.read_csv(url_plzen)
zam_liberec = pd.read_csv(url_liberec)

zam_praha['mesto'] = 'Praha'
zam_plzen['mesto'] = 'Plzeň'
zam_liberec['mesto'] = 'Liberec'

zamestnanci = pd.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)

url_platy = "https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv"
platy = pd.read_csv(url_platy)

zamestnanci_s_platy = pd.merge(zamestnanci, platy, on='cislo_zamestnance', how='left')

print("Rozměry tabulky zaměstnanci:", zamestnanci.shape)
print("Rozměry tabulky platy:", platy.shape)
print("Rozměry spojené tabulky:", zamestnanci_s_platy.shape)

prumerne_platy = zamestnanci_s_platy.groupby('mesto')['plat'].mean()
print("\nPrůměrný plat zaměstnanců v jednotlivých kancelářích:\n", prumerne_platy)

url_vykazy = "https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv"
vykazy = pd.read_csv(url_vykazy)

print("Názvy sloupců ve vykazech:\n", vykazy.columns)

celkove_hodiny_projekty = vykazy.groupby('project')['hours'].sum()
print("\nCelkový počet vykázaných hodin za jednotlivé projekty:\n", celkove_hodiny_projekty)