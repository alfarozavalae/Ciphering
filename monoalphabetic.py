


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
    for line in expo_file:                                      # accessing each line in the file
        words = line.split()                                    # splitting the words in the lines
        for words in monoalpha_cipher:
            if words in monoalpha_cipher:                                    # if the word is in the dictionary
                    result.append(monoalpha_cipher[words])          # each word that is a number will be retrieved and appended to barcode
            else:                                               # otherwise
                for letter in words:                             # each letter will be checked and the numbers will be retrieved
                    if letter in monoalpha_cipher:
                        result.append(monoalpha_cipher[letter])      # the retrieved numbers are appended in the barcode
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
#check the above function
    # text = str(input("What is the text"))
    # text = text.split()
    # # s = int(input("What is the shift?"))
    # # print("Text  : " + text)
    # # print("Shift : " + str(s))
    # choice = input("1 - Encrypt, 2 - Decrypt")
    # if choice == "1":
    encrypt(expo_file="plain.txt")
        # print("Cipher: " + encrypt(text))
    # elif choice == "2":
    #     print("Cipher: " + decrypt(text,s))

main()
