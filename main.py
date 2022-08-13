import time

# ONE SPACE BETWEEN MORSE CODE, TWO SPACES BETWEEN MORSE CODE WORDS

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}


def message(string):
    # Need to run the program as "py -u main.py" for this function to work!
    for i in string:
        print(i, end="")
        time.sleep(0.1)


# cipher
def encrypt(text):
    cipher = ""
    for i in range(len(text)):
        char = text[i].upper()
        try:
            if text[i] + text[i+1] == ", ":
                cipher += MORSE_CODE_DICT[", "]
        except IndexError:
            pass
        if char in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[char] + " "
        elif text[i] == " ":
            cipher += " "
    return cipher


# decipher
def decrypt(cipher):
    if "  " in cipher:
        cipher = cipher.replace("  ", " _ ")
    cipher_letters_list = cipher.split()
    morse_code_in_tuples = MORSE_CODE_DICT.items()

    decipher = ""
    for idx in range(len(cipher_letters_list)):
        if cipher_letters_list[idx] == "_":
            decipher += " "
        for code in morse_code_in_tuples:
            if cipher_letters_list[idx] == code[1]:
                decipher += code[0].upper()
    return decipher


print("ENTER A MESSAGE BELOW")
text = input(">>")
cipher = encrypt(text)
decipher = decrypt(cipher)

message(cipher)
print()
message(decipher)
