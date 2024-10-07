def valitse_lukumaara(monikko):
    kpl = monikko[1]
    return kpl
inventaario = [("aasi", 12), ("muumimuki", 1), ("varsikirves", 4)]
inventaario.sort(key=valitse_lukumaara, reverse=True)
print(inventaario)