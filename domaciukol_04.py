def telefon_cislo_check(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and cislo[:4] == "+420"):    #správný formát a číslo input
        return True
    else:
        return False

def cena_sms(zprava):
    delka_zpravy = len(zprava)
    cena = (delka_zpravy // 180) * 3
    if delka_zpravy % 180 != 0:
        cena += 3
    return cena

telefonni_cislo = input("Zadejte prosím telefonní číslo:")
if telefon_cislo_check(telefonni_cislo):
    zprava = input("Zadejte text zprávy: ")
    cena = cena_sms(zprava)
    print(f"Cena sms: {cena} Kč")
else:
    print("Chybný formát, znovu zkontrolujte telefonní číslo.")