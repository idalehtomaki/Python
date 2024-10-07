def kysy_salasana():
    """
    funktio tarkastaa onko syötetty salasana vähintään 8 merkkiä pitkä
    """
    salasana = ""
    while True:
        salasana = input("Kirjoita salasana: ")
        if len(salasana) < 8:
            print("Salasanan tulee olla vähintään 8 merkkiä pitkä")
        else:
            return salasana
            
print(kysy_salasana())
