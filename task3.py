import os
import shutil

source_folder = "source_images"
destination_folder = "moved_images"
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("Created 'source_images' folder. Please add .jpg files and run again.")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)