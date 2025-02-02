# wordlist.py - Generates a wordlist from 0000 to 999999

# Open the file in write mode
with open("passwords.txt", "w") as file:
    # Loop through numbers from 0000 to 999999
    for i in range(0, 1000000):
        file.write(str(i).zfill(4) + "\n")  # Ensure at least 4-digit format

print("Wordlist generated")