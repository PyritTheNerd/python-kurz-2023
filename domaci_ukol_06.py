class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení auta."
        else:
            return "Vozidlo momentálně není k dispozici."

    def get_info(self):
        return f"Auto s registrační značkou {self.registracni_znacka}, typ vozidla {self.typ_vozidla}"

car1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
car2 = Auto("1P3 4747", "Škoda Octavia", 41253)

while True:
    volba = input("Chcete si půjčit Peugeot nebo Škoda? (Pro ukončení napište 'konec'): ").strip().lower()
    if volba == "konec":
        break

    if volba == "peugeot":
        auto = car1
    elif volba == "škoda":
        auto = car2
    else:
        print("Nesprávná volba. Prosím zadejte jednu z možností: Peugeot nebo Škoda.")
        continue

    vysledek = auto.pujc_auto()
    print(vysledek)
    if vysledek == "Potvrzuji zapůjčení vozidla":
        print("Informace o vozidle:", auto.get_info())
