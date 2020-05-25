
import pickle
from livre import Livre

all_items = []

with open('items.txt', "r") as items:

    for ligne in items:
        livre_name = ligne.strip()
        livre_data_path = livre_name + ".data"
        with open(livre_data_path, "rb") as fic:
            get_record = pickle.Unpickler(fic)
            livre = get_record.load()
            all_items.append(livre)

for item in all_items:
    print(item.nom)

