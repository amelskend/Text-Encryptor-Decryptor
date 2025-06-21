from classical import caesar
from classical import vigenere

def main():
    print("=== Text Encryptor/Decryptor ===")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    choice = input("Choose algorithm: ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter '1' for Caesar Cipher or '2' for Vigenère Cipher.")
        choice = input("Choose algorithm: ")

    if choice == '1':
        user_message = input("Enter your text: ")
        user_key = int(input("Enter your key (e.g. 3): "))
        action = input("Do you want to Encrypt or decrypt (e/d) :")
        action = action.lower()
        while action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            action = input("Do you want to Encrypt or decrypt (e/d) :").lower()
            
        if action == 'e':
            result = caesar.encryption(user_message, user_key)
        else:
            result = caesar.decryption(user_message, user_key)

        print("Result:", result)

    elif choice == '2':
        user_message = input("Enter your text: ")
        user_key = (input("Enter your key: "))
        while not user_key.isalpha():
            print("Invalid key. Please enter a valid alphabetic key.")
            user_key = input("Enter your key: ")
    
        action = input("Do you want to Encrypt or decrypt (e/d) :")
        action = action.lower()
        while action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            action = input("Do you want to Encrypt or decrypt (e/d) :").lower()

        if action == 'e':
            result = vigenere.encryption(user_message, user_key)
        else:
            result = vigenere.decryption(user_message, user_key)

        print("Result:", result)

if __name__ == "__main__":
    main()
