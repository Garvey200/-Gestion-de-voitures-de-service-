class Employe:
 def __init__(self, numero_permis, nom, prenom):
    self.numero_permis = numero_permis
    self.nom = nom
    self.prenom = prenom
    self.voiture_service = None

 def afficher_infos(self):
     print(f"Numero Permis: {self.numero_permis}\nNom: {self.nom}\nPrenom: {self.prenom}")
     if self.voitureService == None:
         print("Aucune voiture")
     else:
         self.voitureService.afficherInformations()


 def affecterVoiture(self, voiture):
        if self.voitureService != None:
            print("Erreur : employe a deja une voiture")
        elif voiture.chauffeur != None:
            print("Erreur : voiture deja attribuee")
        else:
            self.voitureService = voiture
            voiture.chauffeur = self

