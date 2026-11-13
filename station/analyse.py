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
        "unite" : parties[4]
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

def valeurs_du_capteur(releves, nom):
    """Renvoie la liste des valeurs d'un capteur donné."""
    valeurs = []
    for i in releves:
        if i["capteur"] == nom:
            valeurs.append(i["valeur"])
    print(valeurs)
    return valeurs

def moyenne(valeurs):
    """Calcule la moyenne d'une liste, lève une erreur si la liste est vide."""
    if not valeurs:
        raise ValueError("Erreur de valeur")
    return sum(valeurs) / len(valeurs)

def capteurs_disponibles(releves):
    """Renvoie la liste triée et sans doublon des noms de capteurs."""
    capteurs = []
    for i in releves:
        if i["capteur"] not in capteurs:
            capteurs.append(i["capteur"])
    return sorted(capteurs)

def unite_du_capteur(releves, nom):
    """Renvoie l'unité d'un capteur."""
    for i in releves:
        if i["capteur"] == nom:
            return i["unite"]

def resume(releves):
    """Génère un dictionnaire avec le minimum, la moyenne et le maximum par capteur."""
    stats = {}
    for capteur in capteurs_disponibles(releves):
        valeurs = valeurs_du_capteur(releves, capteur)
        if valeurs:
            mini = min(valeurs)
            maxi = max(valeurs)
            moy = moyenne(valeurs)

            stats[capteur] = (mini, moy, maxi)
    return stats

def afficher_resume(releves):
    """Affiche le résumé statistique de tous les capteurs sous forme de tableau."""
    print(f"{'Capteur':<10} | {'Min':>8} | {'Moy':>8} | {'Max':>8} | Unite")

    stats = resume(releves)

    for capteur, valeurs in stats.items():
        mini, moy, maxi = valeurs
        unite = unite_du_capteur(releves, capteur)
        print(f"{capteur:<10} {mini:>8.1f} {moy:>8.1f} {maxi:>8.1f} {unite}")

if __name__ == "__main__":
    releves = charger("station/donnees/releves_septembre.csv")
    print()
    afficher_resume(releves)
