def muotoile_heksaluvuksi(luku, bitit):
    pyoristys = bitit // 4
    heksaluku = hex(luku)
    heksaluku = heksaluku[2:]
    pituus = len(heksaluku)
    
    if pituus < pyoristys:
        etunollat = "0" * (pyoristys - pituus)
        heksaluku = etunollat + heksaluku
    return  heksaluku

try:
    kokonaisluku = int(input("Anna kokonaisluku: "))
    bittien_lkm = int(input("Anna heksaluvun pituus (bittien lukumäärä): "))
    if kokonaisluku < 0 or bittien_lkm <= 0:
        raise ValueError
    muotoiltu_heksaluku = muotoile_heksaluvuksi(kokonaisluku, bittien_lkm)
    print(muotoiltu_heksaluku)
except ValueError:
    print("Kokonaisluku kiitos")
