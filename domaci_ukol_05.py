temperature = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerna_teplota = [sum(den) / len(den) for den in temperature]
ranni_temperature = [den[0] for den in temperature]
nocni_temperature = [den[3] for den in temperature]
poledni_nocni_temperature = [[den[1], den[3]] for den in temperature]

print("Průměrné denní teploty:", prumerna_teplota)
print("Ranní teploty:", ranni_temperature)
print("Noční teploty:", nocni_temperature)
print("Polední a noční teploty:", poledni_nocni_temperature)


