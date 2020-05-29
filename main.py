import pickle
from algo_tri import *
from user_interaction import *
from livre import Livre

all_livre_name = []

# liste contenant tous les item
all_items = []

running = True
print('develloped by Edouard Nicolas')
while running:

    # ouverture du fichier contenant tous les items enregistré
    with open('items.txt', "r") as items:

        # recuperation des  items enregisté
        for ligne in items:
            if ligne != '':
                livre_name = ligne.strip()
                all_livre_name.append(livre_name)
                livre_data_path = 'data/' + livre_name + ".data"
                with open(livre_data_path, "rb") as fic:  # recuperations des instances enregisté de Livrev en bin
                    get_record = pickle.Unpickler(fic)
                    livre = get_record.load()
                    all_items.append(livre)

    choice = choice_input()
    sorted = []
    if choice == '1':
        sorted = bubble_sort_note(all_items)

    elif choice == '2':
        sorted = bubble_sort_note_inverted(all_items)

    elif choice == '3':
        sorted = bubble_sort_nom(all_items)

    elif choice == '4':
        sorted = bubble_sort_nom_inverted(all_items)

    elif choice == '5':
        add_media()
    elif choice == 'q':
        wasted()
        running = False

    if sorted:
        show_in_array(sorted)
        sorted = []
