class Voiture :
    def __init__(self,matricule,annee,marque,kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur=None

    def afficher_infos(self):
        print(f"Matricule: {self.matricule},Annee: {self.annee},Marque: {self.marque},kilometrage:{self.kilometrage}")
        if self.chauffeur==None:
            print("Aucun chauffeur ")
        else:
            print(f"chauffeur: {self.chauffeur.nom},{self.chauffeur.prenom} ")
