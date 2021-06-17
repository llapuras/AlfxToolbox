import os
from PIL import Image

dirPath = r"C:\Users\chenzhuo04\Desktop\newasset\Game\Assets\Megascans\3D_Plants\Chamomile_ujcnejvja_3dplant"
outPath = r"C:\Users\chenzhuo04\Desktop\megascan"
dirList = os.listdir(dirPath)

for (dirname, dirs, files) in os.walk(dirPath):
   for filename in files:
       if filename.endswith('.TGA'):
            print("Opening:"+filename)
            thefile = os.path.join(dirname, filename)
            im = Image.open(thefile)
            width, height = im.size
            im_rgb = im.convert('RGBA') # 可设定RGB或者RBGA

            for x in range(0, width):
                for y in range(0,height):
                    r, g, b, a = im_rgb.getpixel((x, y))
                    im_rgb.putpixel((x, y), (b, a, g, r))

            print("Saving:"+filename)
            outfile = os.path.join(outPath, filename)
            im_rgb.save(outfile, "TGA")  # 注意修改图片格式

print("Finished!")
