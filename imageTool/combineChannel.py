import os
from PIL import Image

dirPath = r"C:\Users\chenzhuo04\Documents\Megascans Library\Downloaded\atlas\plants_Jungle_shzkfcrf2"
dirPath2 = r"C:\Users\chenzhuo04\Documents\Megascans Library\Downloaded\atlas\plants_Jungle_shzkfcrf2"
#outPath = r"C:\Users\chenzhuo04\Desktop\megascan"
outPath = r"C:\Users\chenzhuo04\Documents\Megascans Library\Downloaded\atlas\plants_Jungle_shzkfcrf2"
dirList = os.listdir(dirPath)

for (dirname, dirs, files) in os.walk(dirPath):
   for filename in files:

       if("Albedo" in filename):
           albedo = filename
           print(albedo)

       if("Opacity" in filename):
           opacity = filename
           print(opacity)

   thefile1 = os.path.join(dirname, albedo)
   im1 = Image.open(thefile1)
   width, height = im1.size
   im_rgb1 = im1.convert('RGBA')  # 可设定RGB或者RBGA

   thefile2 = os.path.join(dirname, opacity)
   im2 = Image.open(thefile2)
   im_rgb2 = im2.convert('RGBA')  # 可设定RGB或者RBGA

   for x1 in range(0, width):
       for y1 in range(0, height):
           r1, g1, b1, a1 = im_rgb1.getpixel((x1, y1))
           r2, g2, b2, a2 = im_rgb2.getpixel((x1, y1))
           im_rgb1.putpixel((x1, y1), (r1, g1, b1, r2))

   xx = albedo.replace("Albedo", "Basecolor")
   xx = xx.replace("TGA", "png")

   outfile = os.path.join(dirPath, xx)
   im_rgb1.save(outfile, "PNG")  # 注意修改图片格式

print("Finished!")
