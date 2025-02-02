# Open the file in write mode h
with open("passwords.txt", "w") as file:
    # Loop through numbers from 0000 to 2020
    for i in range(0, 2021):  # Include 2020 by setting the upper limit to 2021
        file.write(str(i).zfill(4) + "\n")  # Ensure each number is zero-padded to 4 digits

print("Wordlist generated")