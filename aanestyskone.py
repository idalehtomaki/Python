def aanesta(sanakirja):
    valinta = input("Anna äänesi, vaihtoehdot ovat:\njaa, ei, eos\n> ").lower()
    if valinta in ["jaa", "ei", "eos"]:
        if valinta == "jaa":
            sanakirja["jaa"] += 1
        elif valinta == "ei":
            sanakirja["ei"] += 1
        elif valinta == "eos":
            sanakirja["eos"] += 1
    else:
        sanakirja["virhe"] += 1
    
def nayta_tulokset(sanakirja):
    print(
          f"\nJaa : {('#' * sanakirja['jaa'])}\n"
          f"Ei : {('#' * sanakirja['ei'])}\n"
          f"Eos : {('#' * sanakirja['eos'])}\n"
          f"Virhe : {('#' * sanakirja['virhe'])}"
          )
          
verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

print("Suoritetaanko verouudistus?")
aanesta(verouudistus)
nayta_tulokset(verouudistus)
print("\nNalle Puh presidentiksi?")
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)
