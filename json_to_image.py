import Utils
import numpy as np
from PIL import Image

# Saves image of prime

jsonFile = "cankut.json"
imgFile = "prime_"+jsonFile.split('.')[0]+".png"

# load from json
num, colors, size = Utils.load_from_file(jsonFile)

# rescale normalized RGB values to 0..255
colors = np.array(colors)*255

# convert num to array of digits
digits = list(map(int,str(num)))

# create rgb array from digits and colors
rgb_array = np.array([colors[d] for d in digits])

# create image
im = Image.frombytes("RGB", size, rgb_array.astype('uint8'))

# save
im.save(imgFile)