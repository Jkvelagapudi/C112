import os
import shutil

from_dir = 'C:/Users/jkvel/Downloads/Doc_Files_Pro_111'
to_dir = 'C:/Users/jkvel/Downloads/Doc_Files_dest'

list_of_files = os.listdir(from_dir)

print(list_of_files)

for i in list_of_files:
    root,exd = os.path.splitext(i)
    print(root,exd)

    if exd == '':
        continue
    elif exd in ['.txt', '.doc', '.docx', '.pdf']:
        print('Moving File...')
        path = from_dir + '/' + i
        if os.path.exists(to_dir):
            shutil.move(path, to_dir)
        else:
            os.makedirs(to_dir)
            shutil.move(path, to_dir)