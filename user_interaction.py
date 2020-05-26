

def choice_input() :
   return input('1 => note croissante\n2 => note décroissante\n3 => Titre ordre alphabetique\n4 => ordre antialphabetique\n>>> ' )

def show_in_array (arr):
    print(' _______________________')
    print(f'| {"titre":10}| {"note":10}|')
    print("|=======================|")

    for item in arr:
        print(f'|{item.nom:10} | {item.note:10}|')
        print('|-----------------------|')
