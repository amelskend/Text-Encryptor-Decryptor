import random
from classical import caesar
from classical import vigenere
from classical import playfair


def main():
    print("=== Text Encryptor/Decryptor ===")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Playfair Cipher")
    choice = input("Choose algorithm: ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter '1', '2', or '3'.")
        choice = input("Choose algorithm: ")

    if choice == '1':  
        user_message = input("Enter your text: ")
        auto_key = input("Do you want to generate a random key? (y/n): ").lower()

        if auto_key == 'y':
            user_key = random.randint(1, 25)  
            print(f"Generated key: {user_key}")
        else:
            user_key = int(input("Enter your key (e.g. 3): "))
            while not (1 <= user_key <= 25):
                print("Invalid key. Please enter a number between 1 and 25.")
                user_key = int(input("Enter your key (e.g. 3): "))

        action = input("Do you want to Encrypt or decrypt (e/d): ").lower()
        while action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            action = input("Do you want to Encrypt or decrypt (e/d): ").lower()

        if action == 'e':
            result = caesar.encryption(user_message, user_key)
        else:
            result = caesar.decryption(user_message, user_key)

        print("Result:", result)

    elif choice == '2':  
        user_message = input("Enter your text: ")
        auto_key = input("Do you want to generate a random key? (y/n): ").lower()
        
        if auto_key == 'y':
            user_key = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(len(user_message)))
            print(f"Generated key: {user_key}")
        else:
            user_key = input("Enter your key: ")
            while not user_key.isalpha():
                print("Invalid key. Please enter a valid alphabetic key.")
                user_key = input("Enter your key: ")

        action = input("Do you want to Encrypt or decrypt (e/d): ").lower()
        while action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            action = input("Do you want to Encrypt or decrypt (e/d): ").lower()

        if action == 'e':
            result = vigenere.encryption(user_message, user_key)
        else:
            result = vigenere.decryption(user_message, user_key)

        print("Result:", result)

    elif choice == '3':  
        user_message = input("Enter your text: ")
        auto_key = input("Do you want to generate a random key? (y/n): ").lower()

        if auto_key == 'y':
            alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            user_key = ''.join(random.sample(alphabet, len(alphabet)))  
            print(f"Generated key: {user_key}")
        else:
            user_key = input("Enter your key: ")
            while not user_key.isalpha():
                print("Invalid key. Please enter a valid alphabetic key.")
                user_key = input("Enter your key: ")

        action = input("Do you want to Encrypt or decrypt (e/d): ").lower()
        while action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            action = input("Do you want to Encrypt or decrypt (e/d): ").lower()

        if action == 'e':
            result = playfair.encryption(user_message, user_key)
        else:
            result = playfair.decryption(user_message, user_key)

        print("Result:", result)


if __name__ == "__main__":
    main()
