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

    type_mesure = parties[2].strip()

    valeur_convertie = float(parties[3].strip())

    if type_mesure == "temperature" and (valeur_convertie < -50 or valeur_convertie > 60):
            raise ValueError(f"Température aberrante: {valeur_convertie}")

    if type_mesure == "humidite" and (valeur_convertie < 0 or valeur_convertie > 100):
        raise ValueError(f"Humidité aberrante: {valeur_convertie}")

    return {
        "horodatage" : parties[0].strip(),
        "capteur" : parties[1].strip(),
        "type" : type_mesure,
        "valeur" : valeur_convertie,
        "unite" : parties[4].strip()
    }




def charger(chemin):
    erreur = 0
    tab_ligne = lire_lignes(chemin)
    releves = []
    ligne_erreur = 2

    for ligne in tab_ligne:
        print(ligne_erreur)
        try:
            releves.append(decouper(ligne))
        except ValueError:
            print(f"Erreur ligne {ligne_erreur} (ValueError) : Valeur abberante")
            erreur += 1
        except IndexError:
            print(f"Erreur ligne {ligne_erreur} (IndexError) : Ligne incomplète")
            erreur += 1

        ligne_erreur += 1
    print(f"{len(releves)} releves charges, {erreur} lignes ignorees")
    return releves

if __name__ == "__main__":
    releves = charger("station/donnees/releves_septembre.csv")
