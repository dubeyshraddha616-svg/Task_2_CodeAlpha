# Move all .jpg files from a folder to a new folder

# import os

# source_folder = "/home/dubeyshraddha616/Coding/jpg_files"
# destination_folder = "/home/dubeyshraddha616/Coding/moved_jpg_files"

# os.makedirs(destination_folder, exist_ok=True)

# count = 0

# for filename in os.listdir(source_folder):
#     if filename.lower().endswith((".jpg", ".jpeg", ".png")):

#         src = os.path.join(source_folder, filename)
#         dst = os.path.join(destination_folder, filename)

#         print(f"Moving {src} -> {dst}")

#         os.rename(src, dst)

#         count = count +1

# print(f"Moved {count} files")





# Extract all email addresses from a .txt file and save them to another file


# import re

# input_file = "input.txt"
# output_file = "emails.txt"

# try:
#     # Read the input file
#     with open(input_file, "r") as file:
#         text = file.read()

#     # Extract email addresses
#     emails = re.findall(
#         r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
#         text
#     )

#     # Remove duplicates
#     emails = list(set(emails))

#     # Save emails to another file
#     with open(output_file, "w") as file:
#         for email in emails:
#             file.write(email + "\n")

#     print(f"{len(emails)} email(s) extracted and saved to '{output_file}'.")

# except FileNotFoundError:
#     print(f"Error: '{input_file}' not found.")
# except Exception as e:
#     print("An error occurred:", e)





# Scrape the title of a fixed webpage and save it

import requests
from bs4 import BeautifulSoup

# Fixed webpage
url = "https://www.python.org"

try:
    # Fetch webpage content
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.title.string.strip()

    # Save title to a file
    with open("title.txt", "w", encoding="utf-8") as file:
        file.write(title)

    print("Webpage title saved successfully!")
    print("Title:", title)

except requests.exceptions.RequestException as e:
    print("Error:", e)