### Based on https://medium.freecodecamp.org/how-to-build-an-image-type-convertor-in-six-lines-of-python-d63c3c33d1db

# PIL : Python Image Library
# Pillow : supports even > Python 3.0.
# pip3 install Pillow


from PIL import Image  # Python Image Library - Image Processing
import glob            # for iterating through files of the given folder in the OS
#print(glob.glob("*.png"))
# based on SO Answer: https://stackoverflow.com/a/43258974/5086335
for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
rgb_im.save(file.replace("png", "jpg"), quality=95)
