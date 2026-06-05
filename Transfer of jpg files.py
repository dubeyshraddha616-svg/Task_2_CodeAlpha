# Move all .jpg files from a folder to a new folder

import os

source_folder = "/home/dubeyshraddha616/Coding/jpg_files"
destination_folder = "/home/dubeyshraddha616/Coding/moved_jpg_files"

os.makedirs(destination_folder, exist_ok=True)

count = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        src = os.path.join(source_folder, filename)
        dst = os.path.join(destination_folder, filename)

        print(f"Moving {src} -> {dst}")

        os.rename(src, dst)

        count = count +1

print(f"Moved {count} files")