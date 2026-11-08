# Project 3: Secret Message Encoder - Caesar Cipher
# Encrypts and decrypts messages by shifting letters in the alphabet.
# Extension 1: Preserve uppercase letters in the original message.

# Step 1: Define lowercase and uppercase alphabets.
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = ALPHABET.upper()

# Step 2: Ask the user to choose an operation.
mode = input("Encrypt (e) or decrypt (d)? ").strip().lower()

# Step 3: Check the selected operation.
if mode == "e":
    print("You selected encryption.")
elif mode == "d":
    print("You selected decryption.")
else:
    print("Invalid choice! Please enter e or d.")

# Step 4: Continue only if the operation is valid.
if mode == "e" or mode == "d":

    # Keep the message exactly as typed: do NOT use .lower() here.
    message = input("Enter your message: ")

    # Convert the shift from text to an integer.
    shift = int(input("Enter shift number: "))

    # Step 5: Decryption shifts letters in the opposite direction.
    if mode == "d":
        shift = -shift

    # Step 6: Start with an empty result.
    result = ""

    # Step 7: Process each character in the message.
    for char in message:

        # Use the uppercase alphabet for capital letters.
        if char.isupper():
            alphabet = UPPER_ALPHABET
        else:
            alphabet = ALPHABET

        # Find the character's position in the chosen alphabet.
        index = alphabet.find(char)

        # Preserve spaces, digits, and punctuation.
        if index == -1:
            result += char
        else:
            # Wrap around when shifting past either end of the alphabet.
            new_index = (index + shift) % 26
            result += alphabet[new_index]

    # Step 8: Show the completed message once, after the loop.
    print(f"Result: {result}")




# Step 9: Testing the program with unusual inputs
#
# Test 1: Empty message
# Operation: Encrypt (e)
# Message: (empty)
# Shift: 5
# Result: Empty output
# Observation: The program runs without errors and returns
# an empty result because there are no characters to encrypt.
#
# Test 2: Zero as input
# Operation: Decrypt (d)
# Message: 0
# Shift: 7
# Result: 0
# Observation: The program leaves the number unchanged
# because digits are not included in the alphabet.
#
# Test 3: Very large numeric message
# Operation: Decrypt (d)
# Message: A very long sequence of numbers
# Shift: 8
# Result: The original numeric message remains unchanged.
# Observation: The program handles long numeric messages
# without errors because numbers are not shifted.
#
# Test 4: Random letters and spaces
# Operation: Encrypt (e)
# Message: Random lowercase letters separated by spaces
# Shift: 3
# Result: Letters were shifted forward by 3 positions.
# Observation: The program successfully encrypts the
# letters while preserving the spaces between words.
#
# Conclusion:
# The Caesar Cipher program successfully handles empty
# messages, numbers, long numeric inputs, and random text.
# It preserves non-alphabetic characters and encrypts
# alphabetic characters according to the selected shift.
