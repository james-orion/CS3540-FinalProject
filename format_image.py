from PIL import Image
import os.path

path = 'C:\\Users\\ralph\\Documents\\Fire' # Change to your path where the images are
dir = os.listdir(path) 

for item in dir:
    fullpath = os.path.join(path,item)
    if os.path.isfile(fullpath):
        im = Image.open(fullpath)

        # Get minimum of width/height
        box = im.getbbox() # returns tuple of dimensions: (0, 0, width, height)
        min_size = min(box[2], box[3])
        
        # Crop and Resize image to 250 by 250
        im = im.crop((0, 0, min_size, min_size))
        im = im.resize((250, 250))
        # Save formatted image
        im = im.convert('RGB') # not sure why this was necessary, but it wouldn't let me save as a jpeg otherwise
        im.save(fullpath, 'JPEG', quality=100)