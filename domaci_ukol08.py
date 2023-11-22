import pandas as pd

file_path = r'C:\Users\root\Desktop\Python kurzy\adopce-zvirat.csv'
data = pd.read_csv(file_path, sep=';')

pocet_radku, pocet_sloupcu = data.shape
print("Počet řádků:", pocet_radku)
print("Počet sloupců:", pocet_sloupcu)
print("Jména sloupců:", ', '.join(data.columns))

zvire_na_indexu_34 = data.at[34, 'Název česky']
print("\nZvíře na indexu 34 (čeština):", zvire_na_indexu_34)
zvire_na_indexu_34_anglicky = data.at[34, 'Název anglicky']
print("Zvíře na indexu 34 (angličtina):", zvire_na_indexu_34_anglicky)

# Bonus
nejdrazsi_adopce = data.sort_values(by='Cena adopce', ascending=False).head(5)
print("\nNejdražší adopce:")
print(nejdrazsi_adopce[['Název česky', 'Cena adopce']])

posledni_cesky = data.sort_values(by='Název česky', ascending=False).iloc[0]['Název česky']
print("\nZvíře alfabeticky poslední v češtině:", posledni_cesky)

posledni_anglicky = data.sort_values(by='Název anglicky', ascending=False).iloc[0]['Název anglicky']
print("Zvíře alfabeticky poslední v angličtině:", posledni_anglicky)
