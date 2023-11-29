import pandas as pd

data = pd.read_csv(r'C:\Users\hanouskovadan\Downloads\temperature.csv')

print("Prvních 5 řádků dat:")
print(data.head())

praha_data = data[data['City'] == 'Prague']
print("\nMěření v Praze:")
print(praha_data)

tepla_data = data[data['AvgTemperature'] > 80]
print("\nMěření s teplotou vyšší než 80 stupňů:")
print(tepla_data)

evropa_tepla_data = data[(data['AvgTemperature'] > 60) & (data['Region'] == 'Europe')]
print("\nMěření s teplotou vyšší než 60 stupňů v Evropě:")
print(evropa_tepla_data)

extremni_data = data[(data['AvgTemperature'] > 80) | (data['AvgTemperature'] < -20)]
print("\nExtrémní hodnoty teploty:")
print(extremni_data)
