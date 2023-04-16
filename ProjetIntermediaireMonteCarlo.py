# Importation des bilibothèques.

import numpy as np 
import random as r
import matplotlib.pyplot as plt

# Définition de la fonction percolation orientée par liens.

def percolation_orientee(probabilite, nb_tests, dim): 
  # Calcul des différentes probabilités de survie.
  probabilites = np.arange(probabilite + 1) / probabilite
  probabilites_survie = []
  for probabilite_actuelle in probabilites:
    percolation_reussie = 0
    # Exécute le test nb_tests fois.
    for num_test in range(nb_tests):
    #Crée un tableau rempli de zéros (dim x dim)
      reseau = np.zeros((dim, dim))
      for i in range(dim):
        for j in range(dim):
          if r.random() <= probabilite_actuelle:
            reseau[i][j] = 1
    # Vérifie s'il existe un chemin de la première à la dernière colonne.
      percolation_reussie += np.sum(reseau[:,0] * reseau[:, dim-1]) > 0
    # Stocke les résultats de chaque test
    probabilites_survie.append(percolation_reussie / nb_tests)
  # Calcul de la variance et de l'écart type
  variance = np.var(probabilites_survie)
  ecart_type = np.sqrt(variance)
  # Calcul de l'erreur (écart type divisé par la racine du nombre de tests)
  erreur = ecart_type / np.sqrt(nb_tests)
  # Graphe et résultats finaux.
  print("Graphique pour la dimension", dim, "affiche.") 
  print("Le seuil de percolation est", probabilites[np.argmax(probabilites_survie)])
  plt.plot(probabilites, probabilites_survie, color='red')
  plt.errorbar(probabilites, probabilites_survie, yerr=erreur, fmt='.', color= 'blue')
  plt.show()

# Appele la fonction percolation_orientée pour différentes dimensions.
for dim in [10, 100 , 1000, 100000]:
  percolation_orientee(100, 100, dim)