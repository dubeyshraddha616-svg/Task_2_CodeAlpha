# Extract all email addresses from a .txt file and save them to another file


import re

input_file = "input.txt"
output_file = "emails.txt"

try:
    # Read the input file
    with open(input_file, "r") as file:
        text = file.read()

    # Extract email addresses
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

#     # Remove duplicates
    emails = list(set(emails))

    # Save emails to another file
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"{len(emails)} email(s) extracted and saved to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
except Exception as e:
    print("An error occurred:", e)