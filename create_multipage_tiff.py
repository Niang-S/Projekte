# Author: Sohibou Niang
# Created on 16.08.2023 at 13:40
## Generate a multipage tiff, gif and pdf from images in a folder
# This has the purpose of comparing the size of the mutipage documents between themselves and to 
# the sum of the size of the standalone images

import io
from PIL import Image
import os

# Define a function to generate the multipage documents
# Inputs are folder_path containing the source images to be used and the different output file formats
def create_multipage_tiff(folder_path, output_path_tiff, output_path_gif, output_path_pdf):
    images = [] # container to host the images in the folder_path
    image_extension = ['.jpg', '.png', '.tiff'] # supported image formats
    # loop to find images names from the folder_path and put the images in the container
    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext)for ext in image_extension):
            image_path = os.path.join(folder_path, filename)
            images.append(Image.open(image_path))
    # Save the images
    if images:
        images[0].save(output_path_tiff, save_all=True, append_images=images[1:])
        images[0].save(output_path_gif, save_all=True, append_images=images[1:], loop=0, duration=200)#loop duration can be varied
        images[0].save(output_path_pdf, save_all=True, append_images=images[1:])


# Define folder containing the images (folder_path)
input_folder = "C:/Users/Niang/Documents/Volume-Test-27/pos02/deltaTL"
# Define output data names for the different formats
output_tiff = "C:/Users/Niang/Documents/Volume-Test-27/pos02/deltaTL/multipage.tiff"
output_gif = "C:/Users/Niang/Documents/Volume-Test-27/pos02/deltaTL/multipage.gif"
output_pdf = "C:/Users/Niang/Documents/Volume-Test-27/pos02/deltaTL/multipage.pdf"
# Call the function
create_multipage_tiff(input_folder, output_tiff, output_gif, output_pdf) 
