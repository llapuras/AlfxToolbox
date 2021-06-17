import os
from PIL import Image


dirPath = r"C:\Users\chenzhuo04\Desktop\sy\origin"
dirList = os.listdir(dirPath)
outPath = r"C:\Users\chenzhuo04\Desktop\sy\output"

for (dirname, dirs, files) in os.walk(dirPath):
   for filename in files:
       if filename.endswith('.jpg'):
            print("Opening:"+filename)
            thefile = os.path.join(dirname,filename)
            im = Image.open(thefile)
            #im.load()

            width, height = im.size

            im_rgb = im.convert('RGB')

            for x in range(0, width):
                for y in range(0,height):
                    r, g, b = im_rgb.getpixel((x, y))
                    im_rgb.putpixel((x, y), (b, g, r))

            print("Saving:"+filename)
            #outfile, ext = os.path.splitext(infile)
            outfile = os.path.join(outPath,filename)
            im_rgb.save(outfile, "JPEG")


print("Ding!")