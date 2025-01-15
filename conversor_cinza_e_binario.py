import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def convert_binary(image_matrix):
    white = 255
    black = 0
    
    initial_conv = np.where((image_matrix <= 127), image_matrix, white)
    final_conv = np.where((initial_conv > 127), initial_conv, black)
    
    return final_conv


img = mpimg.imread('imagem.jpg')  
gray = rgb2gray(img)
bw= convert_binary(gray)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 20))
        
ax1.axis("off")
ax1.title.set_text('Escalas de cinza')
        
ax2.axis("off")
ax2.title.set_text("Binarizado")
        
ax1.imshow(gray, cmap=plt.get_cmap('gray'))
ax2.imshow(bw, cmap=plt.get_cmap('gray'))

plt.show()