import Utils
import numpy as np
from PIL import Image

# Saves annotated image of number

jsonFile = "cankut.json"
imgFile = "ann_"+jsonFile.split('.')[0]+".png"

num, colors, size = Utils.load_from_file(jsonFile)
f = Utils.plot_number(num, colors, size, True, True)
f.savefig(imgFile, bbox_inches='tight')