import os
import pathlib
import shutil
from pillow_heif import register_heif_opener
import time
from PIL import Image

register_heif_opener() #plugin for pillow to open heic


dir_list = os.listdir(os.getcwd())   
main_folders = list()
floors_per_plants = dict()
all_photos_names_list = list()
new_extension = ".jpeg"
concat_photos_path = "nueva_extension"

# execute_question = input("What to execute the algorithm? (Y/n) ")

def photo_scrapper():
    start = time.time()
    for i in dir_list:
        filename,extension_name = os.path.splitext(i)
        if extension_name == ".heic":
            src_path = os.path.join(os.getcwd(),f"{i}")
            photos_name = filename
            dst_path = f".\\{concat_photos_path}\\{photos_name}"
            with Image.open(src_path, mode="r") as im:
                im.convert("RGB").save(dst_path + new_extension,"JPEG")
    
    finish = time.time()
    return print(f"Completed in {round(finish - start,2)} seg")

# if execute_question == 'Y' or execute_question == 'y':
if os.path.exists(".\\" + concat_photos_path):
    pass
else:
    os.makedirs(".\\" + concat_photos_path)

photo_scrapper()

# print(dir_list)

print("Thanks for using sr3m's simple heic to jpeg conversion algorithm")
    
