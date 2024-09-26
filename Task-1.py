def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
def display_separator():
    print("\n" + "-" * 50 + "\n")
def caesar_cipher():
    while True:
        display_separator()
        print("Welcome to the Caesar Cipher Program")
        print("Choose an option:")
        print("1: Encrypt a message")
        print("2: Decrypt a message")
        print("3: Exit the program")
        
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            message = input("\nEnter the message you want to encrypt: ")
            shift = int(input("Enter the shift value (positive number): "))
            encrypted_message = encrypt(message, shift)
            display_separator()
            print(f"Original message: {message}")
            print(f"Shift value: {shift}")
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '2':
            message = input("\nEnter the message you want to decrypt: ")
            shift = int(input("Enter the shift value used during encryption: "))
            decrypted_message = decrypt(message, shift)
            display_separator()
            print(f"Encrypted message: {message}")
            print(f"Shift value: {shift}")
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            display_separator()
            print("Thank you for using the Caesar Cipher Program. Goodbye!")
            break

        else:
            display_separator()
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    caesar_cipher()
