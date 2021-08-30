from PIL import Image
from IPython.display import display
import os

def disp(filename, filepath='_static'):
    pil_im = Image.open(os.path.join(filepath,filename))
    display(pil_im)