import pickle
import csv

# class  definissant chaque livre
class Livre:


    def __init__(self, nom, note):
        self.nom = nom
        self.auteur = auteur
        self.resume = resime
        self.note = note

    def hey(self):
        print(self.nom)

    def save(self):
        with open(self.nom + '.data', 'wb') as fic:
            mon_pickler = pickle.Pickler(fic)
            mon_pickler.dump(self)

        with open('items.txt', 'a') as items:
            items.write("\n" + self.nom)
