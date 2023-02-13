import os 
import shutil 
from_dir = "F:/Python/C102"
to_dir = "F:/Python/C102"
list = os.listdir(from_dir)
for file in list:
    root, ext = os.path.splitext(file)
    if ext == "":
        continue
    if ext in [".gif",'.png',".jpg",".jfif"]:
        path_1 = from_dir+"/"+file
        path_2 = to_dir+"/"+"images"
        path_3 = to_dir+"/"+"images"+"/"+file
        if(os.path.exists(path_2)):
            shutil.move(path_1, path_3)
        else:
            os.mkdir(path_2)
            shutil.move(path_1,path_3)
