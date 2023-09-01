import imageio
import os
# for all jp2 files in the folder
# create a new folder named converted
os.mkdir('./converted')
for file in os.listdir('./'):
    if file.endswith('.jp2'):
        # read the jp2 file
        image = imageio.imread('./' + file)
        # write the jpeg file
        imageio.imsave( './converted/' +file + '.jpg', image)