import math

def laske_nelio_ala(sivun_pituus):
    ala = sivun_pituus ** 2
    return ala

def laske_sektorin_ala(sade, sisakulma):
    sisakulma_radiaaneina = sisakulma * (math.pi / 180)
    ala = sisakulma_radiaaneina * (sade ** 2) / 2
    return ala

def laske_sivun_pituus(hypotenuusa):
    sivun_pituus = math.sqrt(hypotenuusa ** 2 / 2)
    return sivun_pituus

def laske_kuvion_ala(x):
    pieni_nelio_ala = laske_nelio_ala(x)
    kolmio_sivu = laske_sivun_pituus(x)
    kolmio_ala = kolmio_sivu ** 2 / 2
    pieni_sektori_ala = laske_sektorin_ala(kolmio_sivu, 45)
    iso_nelio_ala = laske_nelio_ala(kolmio_sivu * 2)
    iso_sektori_ala = laske_sektorin_ala(kolmio_sivu * 2, 90)
    iso_ympyra_ala = math.pi * (kolmio_sivu * 2) ** 2
    ala_summa = (pieni_nelio_ala + kolmio_ala + pieni_sektori_ala 
                 + iso_nelio_ala + iso_ympyra_ala - iso_sektori_ala)   
    return ala_summa

x_pituus = float(input("Anna x: "))
kuvio_ala = laske_kuvion_ala(x_pituus)
kuvio_ala_pyoristetty = round(kuvio_ala, 4)
print(f"Kuvion ala: {kuvio_ala_pyoristetty}")
