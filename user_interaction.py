import os
from livre import Livre
def choice_input() :
   return input('1 => note croissante\n2 => note décroissante\n3 => Titre ordre alphabetique\n4 => ordre antialphabetique\n5 => ajouter un nouveau livre\nq => quiter\n>>> ' )

def show_in_array (arr):
    print(' _______________________________________________________________________________________________________________________________________')
    print(f'| {"titre":40}| {"auteur":40} | {"résume":40} | {"note":6}|')
    print     ("|=========================================|==========================================|==========================================|=======|")

    for item in arr:
        print(f'|{item.nom:40} | {item.auteur:40} | {item.resume:40} | {item.note:6}|')
        print('|-----------------------------------------|------------------------------------------|------------------------------------------|-------|')

def add_media():
    path  = input('veuiller indiquez le chemin du fichier\n>>>')
    auteur = input("indiquez l'auteur\n>>>" )
    note = input("indiquez la note de ce fichier\n>>>")
    resume = input("inidquez un résumé\n>>>")
    filename, fileExtension = os.path.splitext(path)
    Livre(filename, note, auteur, resume, path, fileExtension).save()