# move input images around for training the second discriminator
import os

direction = 'BtoA'
fil = open(direction+"-discriminator-values.txt", 'r')
new_directory = 'beer2juice2'


images = []
for line in fil:
  l = line.strip().split(',')
  images.append((float(l[1]), l[0]))
images.sort()

print images
for img in images[int(-1* 0.6*len(images)) :]:
  fil = img[1].split('/')[-1]
  print "./datasets/"+new_directory+"/train"+direction[0]+"/"+fil
  os.remove("./datasets/"+new_directory+"/train"+direction[0]+"/"+fil)



