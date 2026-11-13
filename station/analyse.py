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

    type_mesure = parties[2]

    valeur_convertie = float(parties[3])

    if type_mesure == "temperature" and (valeur_convertie < -50 or valeur_convertie > 60):
            raise ValueError(f"Température aberrante: {valeur_convertie}")

    if type_mesure == "humidite" and (valeur_convertie < 0 or valeur_convertie > 100):
        raise ValueError(f"Humidité aberrante: {valeur_convertie}")

    return {
        "horodatage" : parties[0],
        "capteur" : parties[1],
        "type" : type_mesure,
        "valeur" : valeur_convertie,
        "unite" : parties[4]
    }




def charger(chemin):
    erreur = 0
    tab_ligne = lire_lignes(chemin)
    releves = []

    for ligne in tab_ligne:
        try:
            releves.append(decouper(ligne))
        except ValueError:
            erreur += 1
        except IndexError:
            erreur += 1
    print(erreur," erreurs ", len(releves), "releves charges")

    return releves

if __name__ == "__main__":
    releves = charger("donnees/releves_septembre.csv")
