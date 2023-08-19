import os
import shutil

from_dir = "111"
to_dir = "1111"

list_of_files = os.listdir(from_dir)
print(list_of_files)

name, extension = os.path.splitext(file_name)