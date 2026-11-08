
# Project 3: Secret Message Encoder - Caesar Cipher
# This program encrypts and decrypts messages
# by shifting letters through the alphabet.

# Step 1: Define the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Step 2: Ask the user to choose an operation
mode = input("Encrypt (e) or decrypt (d)? ").lower()

# Step 3: Check which operation the user selected
if mode == "e":
    print("You selected encryption.")

elif mode == "d":
    print("You selected decryption.")

# Step 4: Continue only if the choice is valid
if mode == "e" or mode == "d":

    # Ask the user to enter a message
    # .lower() converts capital letters to lowercase
    message = input("Enter your message: ").lower()

    # Ask how many positions to shift
    # int() converts the input into a whole number
    shift = int(input("Enter shift number: "))

    # Step 5: Reverse the shift for decryption
    # Encryption moves forward (+)
    # Decryption moves backward (-)
    if mode == "d":
        shift = -shift

    # Step 6: Create an empty string for the result
    result = ""

    # Step 7: Process every character in the message
    for char in message:

        # Find the character's position in the alphabet
        index = ALPHABET.find(char)

        # If the character is not in the alphabet,
        # keep it unchanged (spaces, numbers, punctuation)
        if index == -1:
            result += char

        else:
            # Calculate the new position
            # % 26 makes letters wrap around the alphabet
            new_index = (index + shift) % 26

            # Get the new letter and add it to the result
            result += ALPHABET[new_index]

    # Step 8: Print the completed message
    print(f"Result: {result}")
