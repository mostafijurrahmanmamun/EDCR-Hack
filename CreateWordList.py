Open the file in write mode
with open("passwords.txt", "w") as file:
    # Loop through numbers from 0000 to 2020
    for i in range(0, 2020):
        file.write(str(i).zfill(4) + "\n")  # Ensu>

print("Wordlist generated")