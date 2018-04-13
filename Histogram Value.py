from PIL import Image
import glob
s = []

for img in glob.glob("Folder Name/*.jpg"):
    im = Image.open(img)
    s.append(im.histogram())

with open("File Name.txt", "w") as output:
    output.write(str(s))
