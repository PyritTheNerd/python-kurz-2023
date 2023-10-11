sklad = {          #stav skladu
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

def nakup(sklad):
    kod_soucastky = input("Zadejte kód: ")

    if kod_soucastky in sklad:
        mnozstvi = int(input("Zadejte požadované množství: "))

        if sklad[kod_soucastky] < mnozstvi:
            print("Lze prodat pouze omezené množství kusů.")
            del sklad[kod_soucastky]
        else:
            print("Poptávku lze uspokojit v plné výši.")
            sklad[kod_soucastky] -= mnozstvi
    else:
        print("Není skladem.")

nakup(sklad)

print("Aktuální stav skladu:")
for soucastka, mnozstvi in sklad.items():
    print(f"{soucastka}: {mnozstvi}")