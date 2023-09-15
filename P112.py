import os
import shutil

destination = 'C:/Users/Sanjay/Downloads'
source = 'C:/Users/Sanjay/Desktop/Document_Files'

files = os.listdir(source)

for i in files:
    name,ext = os.path.splitext(i)

    if ext == '':
       continue

    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + i

        if os.path.exists(path2):
            print(f"Moving {i} ...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print(f"Moving {i} ...")
            shutil.move(path1, path3)
        

print(name, ext)

