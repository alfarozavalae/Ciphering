#############################################################################################3
# Code created by Emely and Ela

###############################################################################################


def encrypt(expo_file):
    monoalpha_cipher = {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'u',
    's': 'v',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c'}
    result = []
    for i in expo_file:                                      # accessing each line in the file
        for key, value in monoalpha_cipher:
            if key in monoalpha_cipher:                                    # if the word is in the dictionary
                    result. append(monoalpha_cipher[value])          # each word that is a number will be retrieved and appended to barcode
            else:                                               # otherwise
                for letter in key:                             # each letter will be checked and the numbers will be retrieved
                    if letter in monoalpha_cipher:
                        result. append(monoalpha_cipher[letter])     # the retrieved numbers are appended in the barcode
    print(result)
    return result


def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Decrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

def main():

    expo_file = input("enter string")
    expo_file = expo_file.split()
    print(expo_file)
    encrypt(expo_file)
main()
