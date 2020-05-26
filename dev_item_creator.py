#ce module est temporaire.
# il permet de creer est instance de Livre sans polluer
# 'main.py' durant devellopement de ce projet tant que la fonction d'ajout d'item
# ne sera pas implémanté.


from livre import Livre
Livre('pierre', 50, 'pierro', 'reusmé de super qualité').save()