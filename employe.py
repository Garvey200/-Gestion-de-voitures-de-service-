class Employe:
 def __init__(self, numero_permis, nom, prenom):
    self.numero_permis = numero_permis
    self.nom = nom
    self.prenom = prenom
    self.voiture_service = None

 def afficher_infos(self):
     print(f"Numero Permis: {self.numero_permis}\nNom: {self.nom}\nPrenom: {self.prenom}")
     if self.voiture_service == None:
         print("Aucune voiture")

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





