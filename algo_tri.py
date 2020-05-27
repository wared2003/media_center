#ce fichier contien tous les algorythmes de tri


### les fonctions suivantes prennent en parametre une liste d'objet et retourne une liste d'objet

# tri par ordre croissant selon la note
def bubble_sort_note(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if int(arr[j].note) > int(arr[j + 1].note):
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

# tri par ordre decroissant selon la note

def bubble_sort_note_inverted(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if int(arr[j].note) < int(arr[j + 1].note):
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

# tri par ordre alphabetique selon le titre

def bubble_sort_nom(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j].nom > arr[j + 1].nom:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

# tri par ordre antialphabetique selon le titre

def bubble_sort_nom_inverted(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j].nom < arr[j + 1].nom:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr