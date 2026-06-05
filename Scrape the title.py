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