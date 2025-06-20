from classical import caesar

def main():
    print("=== Text Encryptor/Decryptor ===")
    print(" Caesar Cipher")
    user_message = input("Enter your text: ")
    shift = int(input("Enter your key (e.g. 3): "))
    choice = input("Do you want to Encrypt or decrypt (e/d) :")
    choice = choice.lower()
    while choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        choice = input("Do you want to Encrypt or decrypt (e/d) :").lower()
    if choice == 'e':
        result = caesar.encryption(user_message, shift)
    else:
        result = caesar.decryption(user_message, shift)

    print("Result:", result)

if __name__ == "__main__":
    main()
