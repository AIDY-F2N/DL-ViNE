
import matplotlib.pyplot as plt
import numpy as np

#RUNTIME ******************************************************************************
# Données
algorithms = [ 'NEPA(path)', 'NRPA-DL', 'DL-ViNE']
runtimes = [0.4567615895895636, 0.3574469684108364,  0.2832534573542909]  # Temps d'exécution (en secondes)

# Création du graphique en barres horizontales
fig, ax = plt.subplots(figsize=(8, 4))  # Taille plus grande pour plus de clarté

y_pos = np.arange(len(algorithms))

# Amélioration des couleurs avec une palette plus douce et des bordures autour des barres
bars = ax.barh(y_pos, runtimes, color='steelblue', edgecolor='black')

# Ajout des étiquettes
ax.set_yticks(y_pos)
ax.set_yticklabels(algorithms, fontsize=12)
ax.invert_yaxis()  # Le premier en haut

# Ajouter un titre et une légende des axes
ax.set_xlabel('Runtime per slice (seconds)', fontsize=12)

# Ajouter des annotations pour chaque barre (afficher la valeur)
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.02, bar.get_y() + bar.get_height()/2, 
            f'{width:.2f}', va='center', ha='left', fontsize=10)

# Ajuster les limites de l'axe X
ax.set_xlim([0, 1])

# Supprimer les bordures autour du graphique
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajouter un peu d'espace autour du graphique
plt.tight_layout()

# Affichage du graphique
plt.show()