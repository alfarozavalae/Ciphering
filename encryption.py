__author__ = 'heggens'
'''
This program implements three encryption algorithms:
Simple cipher, stream cipher, and a block cipher
'''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key_real = 'defghijklmnopqrstuvwyyz'


def encryptSimpleCipher(pt, key):
    output = 0
    pt.read()
    for i in pt:
        if i in alphabet:
            old_letter = alphabet.find(i)
            output += alphabet[(old_letter + key) % 26]
        else:
            output += i         # Adds non-alphabet characters directly
    # TODO encrypt the simple cipher. Save the output to a new file and return it to the calling function.
    print(output)


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
    plainText = open('plainText.txt', 'r')

    outputCipher = encryptSimpleCipher(plainText, 3)
    #outputCipher = encryptStreamCipher(plainText, key)
    #outputCipher = encryptBlockCipher(plainText, key)
    print("The encrypted message is: {}".format(outputCipher))

    ########################################################################

    # Now, we'll assume we are the receiver, and want to decrypt the message
    #outputPlain = decryptSimpleCipher(outputCipher, key)
    # outputPlain = decryptStreamCipher(outputCipher, key)
    # outputPlain = decryptBlockCipher(outputCipher, key)
    #print ("The received message is: {}".format(outputPlain))


main()
