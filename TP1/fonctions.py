def calculer_ttc(prix_ht, tva):
    return prix_ht + prix_ht * tva

def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) >= 8 and any(c.isupper() for c in mot_de_passe) and any(c.isdigit() for c in mot_de_passe):
        return True
    return False

def convertir_date(date_fr):
    jour, mois, annee = date_fr.split('/')
    return f"{annee}-{mois}-{jour}"
