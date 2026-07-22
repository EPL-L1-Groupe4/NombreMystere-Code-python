import random
from traceback import print_tb

nbre_myster = random.randint(1, 100)


def Jeux():
    cpt=1
    print("==================================================")
    print("                    Jeux                          ")
    print("==================================================")

    utilisateur = int(input("Entrer un nombre : "))
    while cpt>0:
        if utilisateur == nbre_myster:

            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Felicitation vous avez deviner")

            print("Voulez-vous continuer?\n1.continuer\n2.arretter")
            choice=int(input("choix : "))
            if choice==1:
                utilisateur = int(input("Entrer un nombre : "))
            elif choice==2:
                break

        elif utilisateur < nbre_myster:
            print("Le nombre plus petit que le nombre mystere")
            utilisateur = int(input("Ressayer .Entrer un nombre : "))

        elif utilisateur > nbre_myster:
            print("Le nombre plus grand que le nombre mystere")
            utilisateur = int(input("Ressayer .Entrer un nombre : "))
        cpt+=1
    print(" Merci d'avoir participer")

print("================================================")
print("BIENVENU DANS LE PROGRAMME DE SAKPANI PAGUIYEDOU")
print("================================================")

print("|------------------------------------------------------------------------------------------------|")
print("|Pagui vous presente un jeux surnomé  le nombre  mystere                                         |")
print("|la logique consiste a determiner un nombre compris entre \n\tdeux intervalles [1, 100]          |")

print("|Vous etes chaud a voyager avec moi ? Si OUI appuiyez la touche 1 sinon la 0                     |")
print("|------------------------------------------------------------------------------------------------|")

##print(f"Nombre mystere:{nbre_myster}")
print("1.OUI\n0.NON")
choix=int(input("choix: "))
if choix==1:
    Jeux()
if choix==0:
    print("A bientot")