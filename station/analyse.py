def lire_lignes(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    lignes_propres = []

    for ligne in lignes[1:]:
        ligne_nettoyee = ligne.strip()

        if ligne_nettoyee: #Vérifie si liste non vide
            lignes_propres.append(ligne_nettoyee)

    return lignes_propres

def decouper(ligne):
    parties = ligne.split(",")

    return {
        "horodatage" : parties[0],
        "capteur" : parties[1],
        "type" : parties[2],
        "valeur" : float(parties[3]),
        "unite" : parties[4]
    }

def charger(chemin):
    tab_ligne = lire_lignes(chemin)
    releves = []

    for ligne in tab_ligne:
        releves = decouper(ligne)
    print(len(releves))

    return releves

if __name__ == "__main__":
    releves = charger("donnees/releves_septembre.csv")
