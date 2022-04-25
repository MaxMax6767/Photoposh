from PIL import Image
import numpy as np

# Ouverture Image
i = Image.open("bmp3(1).bmp")

# Matrice de Pixels
c = np.asarray(i)
print(c)

# Taille (Largeur, Hauteur)
print(i.size)

# DPI & Comresssion
print(i.info)

# Format d'image
print(i.format)



