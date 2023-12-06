import pandas as pd
import matplotlib.pyplot as plt

# Část 1: Histogram platů za únor 2021
platy_url = "C:/Users/hanouskovadan/Desktop/Github repozitář kurz python/python-kurz-2023/platy_2021_02.csv"
platy = pd.read_csv(platy_url)

# Nastavení hranic skupin histogramu
bins = [0, 50000, 75000, 100000, 125000, 150000, 200000, 250000, 300000]

# Vytvoření histogramu
plt.hist(platy['plat'], bins=bins, edgecolor='black')
plt.title('Histogram platů za únor 2021')
plt.xlabel('Plat')
plt.ylabel('Počet zaměstnanců')
plt.show()

# Nepovinný bonus 1: Krabicový graf teplot v městech
temperature_url = "https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv"
teploty = pd.read_csv(temperature_url)

# Zvol sloupec, který obsahuje informace o městech
mesto_sloupec = 'City'  # Změňte na odpovídající název sloupce

# Výběr údajů pro města Helsinki, Miami Beach a Tokyo
vybrane_mesta = teploty[teploty[mesto_sloupec].isin(['Helsinki', 'Miami Beach', 'Tokyo'])]

# Vytvoření krabicového grafu
plt.figure(figsize=(10, 6))
plt.boxplot([vybrane_mesta[vybrane_mesta[mesto_sloupec] == mesto]['AvgTemperature'] for mesto in ['Helsinki', 'Miami Beach', 'Tokyo']],
            labels=['Helsinki', 'Miami Beach', 'Tokyo'])
plt.title('Krabicový graf teplot v městech')
plt.xlabel('Město')
plt.ylabel('Teplota (°C)')
plt.show()
