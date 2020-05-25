
import pickle
from livre import Livre


#liste contenant tous les item
all_items = []

# ouverture du fichier contenant tous les items enregistré
with open('items.txt', "r") as items:

# recuperation des  items enregisté
    for ligne in items:
        livre_name = ligne.strip()
        livre_data_path = livre_name + ".data"
        with open(livre_data_path, "rb") as fic:  # recuperations des instances enregisté de Livrev en bin
            get_record = pickle.Unpickler(fic)
            livre = get_record.load()
            all_items.append(livre)

# affichage des items
for item in all_items:
    print(item.nom)

