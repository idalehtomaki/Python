from math import radians, cos, sin

def muunna_xy_koordinaateiksi(kulma, vektori_pituus):
    x = round(vektori_pituus * cos(kulma), 0)
    y = round(vektori_pituus * sin(kulma), 0)
    x = int(x)
    y = int(y)
    return x, y

def kysy_liike(sanakirja):
    print(f"Hahmo on sijainnissa ({sanakirja['x']}, {sanakirja['y']})")
    sanakirja["suunta"] = float(input("Anna liikkumissuunta asteina: "))
    sanakirja["nopeus"] = float(input("Anna liikenopeus: "))

def paivita_sijainti(sanakirja):
    x_radiaaneina = radians(sanakirja["suunta"])
    sanakirja["x"] += muunna_xy_koordinaateiksi(x_radiaaneina, sanakirja["nopeus"])[0]
    sanakirja["y"] += muunna_xy_koordinaateiksi(x_radiaaneina, sanakirja["nopeus"])[1]
    print(f"Uusi sijainti: ({sanakirja['x']}, {sanakirja['y']})")
    
hahmo_1 = {
    "x": 0,
    "y": 0,
    "suunta": 0,
    "nopeus": 0
}

hahmo_2 = {
    "x": 50,
    "y": 50,
    "suunta": 0,
    "nopeus": 0
}
print("Pelaajan 1 vuoro")
kysy_liike(hahmo_1)
paivita_sijainti(hahmo_1)
print("Pelaajan 2 vuoro")
kysy_liike(hahmo_2)
paivita_sijainti(hahmo_2)
