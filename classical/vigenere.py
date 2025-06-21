def encryption(message, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    i = 0
    for char in message.upper():
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            char_code = ord(char)
            new_char_code = (char_code - ord('A')+ shift) % 26 + ord('A')
            result += chr(new_char_code)
            i = (i + 1) % key_length
        else:
            result += char

    return result


def decryption(cipher, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    i = 0

    for char in cipher.upper():
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            char_code = ord(char)
            new_char_code = (char_code - ord('A') - shift) % 26 + ord('A')
            result += chr(new_char_code)
            i = (i + 1) % key_length
        else:
            result += char

    return result