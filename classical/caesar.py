def encryption(message, shift):
    result = ""

    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > ord("Z"):
                new_char_code -= 26

            if new_char_code < ord("A"):
                new_char_code += 26

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result


def decryption (cipher, shift):
    return encryption(cipher, -shift)