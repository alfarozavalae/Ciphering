__author__ = 'heggens'
'''
This program implements three encryption algorithms:
Simple cipher, stream cipher, and a block cipher
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key_real = 'defghijklmnopqrstuvwyyzabc'


def encryptSimpleCipher(pt, key, filename):
    output = 0
    pt.read()
    for i in pt:
        if i in alphabet:
            old_letter = alphabet.find(i)
            output += alphabet[(old_letter + key) % 26]
        else:
            output += i         # Adds non-alphabet characters directly
            f = open(filename, "w")
            f.write(filename)
            f.close()

    # TODO encrypt the simple cipher. Save the output to a new file and return it to the calling function.

def export_file(key):
    """
    Exports a file called filename

    :param text_to_export: the string to be written to the exported file
    :param filename: a string representing the name of the file to be exported to
    """
    output = ""
    cipher = " "
    for i in cipher:
        if i.upper() in alphabet:
            new_letter = alphabet.find(i.upper())
            output += alphabet[new_letter - key % 26]
        else:
            output += i     # Adds non-alphabet characters directly
    if __name__ == "__main__":
        print("Message Decrypted")
    return output           # Obviously this should output something else





def encryptStreamCipher(plainText, key):
    output = ""
    # TODO encrypt the stream cipher. Save the output to a new file and return it to the calling function.
    return output


def encryptBlockCipher(plaintext, key):
    output = ""
    # TODO encrypt the block cipher. Save the output to a new file and return it to the calling function.
    return output


def decryptSimpleCipher(cipherText, key):
    output = ""
    # TODO decrypt the simple cipher. Save the output to a new file and return it to the calling function.
    return output


def decryptStreamCipher(cipherText, key):
    output = ""
    # TODO decrypt the stream cipher. Save the output to a new file and return it to the calling function.
    return output


def decryptBlockCipher(cipherText, key):
    output = ""
    # TODO decrypt the block cipher. Save the output to a new file and return it to the calling function.
    return output


def main():
    #key = open('key.txt').read()

    # First, we'll assume we are the sender, and want to encrypt a message
    plainText = open('plain.txt', 'r')
    encryptSimpleCipher(plainText, 3, "newone.txt")





    #outputCipher = encryptStreamCipher(plainText, key)
    #outputCipher = encryptBlockCipher(plainText, key)

    ########################################################################

    # Now, we'll assume we are the receiver, and want to decrypt the message
    #outputPlain = decryptSimpleCipher(outputCipher, key)
    # outputPlain = decryptStreamCipher(outputCipher, key)
    # outputPlain = decryptBlockCipher(outputCipher, key)
    #print ("The received message is: {}".format(outputPlain))


main()
