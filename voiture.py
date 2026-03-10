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

    def affecter_voiture(self, voiture):
        if self.voiture_service is None:
            print(f"Voiture attribuée à : {self.nom}")

        else:
            print("Cet employé possède deja une voiture.")

    def retirer_voiture(self):
        if self.voiture_service is not None:
            print(f"voiture retirée pour, {self.nom}")

        else:
            print("Cet employé n'a pas de voiture.")

