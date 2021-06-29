import os
target_folder = r'C:\\User\\Ahnaf\\Download' + "\\"
src_folder = r'I:\\test' + '\\'
for path, dir, files in os.walk(src_folder):
    print(path)
    print(files)
