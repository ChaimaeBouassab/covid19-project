import numpy as np

class ProfilCivil:
    def __init__(self, cni, nom, prenom, date_naissance, genre, situation_familiale):
        self.cni = cni
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.genre = genre
        self.situation_familiale = situation_familiale


class Coordonnee:
    def __init__(self, adresse, ville, region, tel, email):
        self.adresse = adresse
        self.ville = ville
        self.region = region
        self.tel = tel
        self.email = email


class ProfilSanitaire:
    def __init__(self, groupe_sanguin, nbre_maladies_chroniques, nbre_symptomes, test,
                 date_debut_hospitalisation, date_fin_hospitalisation, etat_sortie):
        self.groupe_sanguin = groupe_sanguin
        self.nbre_maladies_chroniques = nbre_maladies_chroniques
        self.nbre_symptomes = nbre_symptomes
        self.test = test
        self.date_debut_hospitalisation = date_debut_hospitalisation
        self.date_fin_hospitalisation = date_fin_hospitalisation
        self.etat_sortie = etat_sortie


class Citoyen:
    def __init__(self, profil_civil, coordonnee, profil_sanitaire):
        self.profil_civil = profil_civil
        self.coordonnee = coordonnee
        self.profil_sanitaire = profil_sanitaire

class Fichier:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier

    def enregistrer_citoyen(citoyen, nom_fichier):
        with open(nom_fichier, 'a') as file:
            # Enregistrement des informations du profil civil
            profil_civil = citoyen.profil_civil
            ligne = f"{profil_civil.cni},{profil_civil.nom},{profil_civil.prenom}"

            # Enregistrement des informations de la date de naissance
            date_naissance = profil_civil.date_naissance
            ligne += f"#{date_naissance.jour}/{date_naissance.mois}/{date_naissance.annee}"

            # Enregistrement des informations des coordonnées
            coordonnee = citoyen.coordonnee
            ligne += f"#{coordonnee.adresse},{coordonnee.ville},{coordonnee.region},{coordonnee.email}"

            # Enregistrement des informations du profil sanitaire
            profil_sanitaire = citoyen.profil_sanitaire
            ligne += f"&{profil_sanitaire.groupe_sanguin},{profil_sanitaire.nbre_maladies_chroniques}," \
                     f"{profil_sanitaire.nbre_symptomes},{profil_sanitaire.test}," \
                     f"{profil_sanitaire.date_debut_hospitalisation},{profil_sanitaire.date_fin_hospitalisation}," \
                     f"{profil_sanitaire.etat_sortie}"

            file.write(ligne + '\n')
class Statistiques:
    def __init__(self, fichier):
        self.fichier = fichier

    def calculer_nombre_citoyens_enregistres(self):
        count = 0
        with open(self.fichier.nom_fichier, 'r') as file:
            for line in file:
                count += 1
        return count

    def calculer_nombre_citoyens_testes_positifs(self):
        count = 0
        with open(self.fichier.nom_fichier, 'r') as file:
            for line in file:
                if "&2" in line:
                    count += 1
        return count

def calculer_duree_moyenne_hospitalisation(hospitalisations):
    durees = [hospitalisation.duree for hospitalisation in hospitalisations]
    duree_moyenne = np.mean(durees)
    return duree_moyenne

def calculer_ecart_type_var_hospitalisation(hospitalisations):
    durees = [hospitalisation.duree for hospitalisation in hospitalisations]
    ecart_type = np.std(durees)
    variance = np.var(durees)
    return ecart_type, variance
def messages_count_all(self):
        users = {}
        for line in open('messages.txt'):
            if line.__contains__(self.session.name):
                message_line = line.split(',')
                if message_line[1] == self.session.name:
                    if message_line[3][0] == '0':
                        users[message_line[0]] = 0
        return len(users)



               