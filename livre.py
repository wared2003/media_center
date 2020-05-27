import pickle
import csv

# class  definissant chaque livre
class Livre:

# initialisation des attributs de livre
    def __init__(self, nom, note, auteur, resume, path, filetype):
        self.nom = nom
        self.auteur = auteur
        self.resume = resume
        self.note = note
        self.path = path
        self.filetype = filetype

    # methode temporaire servant au deboguage
    def hey(self):
        print(self.nom)

    # methode  permetant de sauvegardé l'objet courant en bin
    def save(self):
        with open('data/' + self.nom + '.data', 'wb') as fic:
            mon_pickler = pickle.Pickler(fic)
            mon_pickler.dump(self)

        with open('items.txt', 'a') as items:
            items.write("\n" + self.nom)
