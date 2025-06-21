def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used = set()

    for char in key + alphabet:
        if char not in used:
            matrix.append(char)
            used.add(char)
        if len(matrix) == 25:
            break

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def prepare_message(message):

    message = message.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0

    while i < len(message):
        a = message[i]
        b = message[i + 1] if i + 1 < len(message) else "X"

        if a == b:
            prepared += a + "X"
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += "X"

    return prepared


def encryption(message, key):

    matrix = generate_key_matrix(key)
    message = prepare_message(message)
    result = ""

    for i in range(0, len(message), 2):
        a, b = message[i], message[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            result += matrix[row_a][(col_a + 1) % 5]
            result += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            result += matrix[(row_a + 1) % 5][col_a]
            result += matrix[(row_b + 1) % 5][col_b]
        else:
            result += matrix[row_a][col_b]
            result += matrix[row_b][col_a]

    return result


def decryption(cipher, key):
    matrix = generate_key_matrix(key)
    result = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            result += matrix[row_a][(col_a - 1) % 5]
            result += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            result += matrix[(row_a - 1) % 5][col_a]
            result += matrix[(row_b - 1) % 5][col_b]
        else:
            result += matrix[row_a][col_b]
            result += matrix[row_b][col_a]

    return result