from voiture import Voiture
from employe import Employe

e1=Employe("p125","Jhon","Dagrun")
e2=Employe("p129","Nadia","Shafo")

v1=Voiture("AA123","2025","Toyota",50000)
v2=Voiture("BB689","2026","BMW",56)

e1.afficher_infos()
e2.afficher_infos()

v1.afficher_infos()
v2.afficher_infos()

print("\nAprès affectation : \n ")
e2.affecter_voiture(v1)
v1.afficher_infos()

print("\n Après retrait : \n")
e2.retirer_voiture()
