
import pickle
from algo_tri import *
from user_interaction import *
from livre import Livre

all_livre_name = []

#liste contenant tous les item
all_items = []

# ouverture du fichier contenant tous les items enregistré
with open('items.txt', "r") as items:

# recuperation des  items enregisté
    for ligne in items:
        livre_name = ligne.strip()
        all_livre_name.append(livre_name)
        livre_data_path = 'data/' + livre_name + ".data"
        with open(livre_data_path, "rb") as fic:  # recuperations des instances enregisté de Livrev en bin
            get_record = pickle.Unpickler(fic)
            livre = get_record.load()
            all_items.append(livre)

# affichage des items
#for item in all_items:
#    print(item.nom)

tri = bubble_sort_nom_inverted(all_items)
show_in_array(tri)

