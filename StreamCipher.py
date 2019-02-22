def encryptStreamCipher(plainText, word):
    """uses plaintext, and returns an encrypted string"""
    cipherText = ""
    plainText = plainText.lower()
    key = ("hello")
    count = 0

    for ch in plainText:
        if count >= len(key): #ensures that the function constantly uses the key
            count = 0
        if ch.isalpha():
            stayInAlphabet = ord(ch) + count(key)
            count = count + 1

            if stayInAlphabet > ord('z'): # keeps the encrypted letter from going above z
                stayInAlphabet -= 26
        else:
            stayInAlphabet = ord(ch)
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print("Your encrypted stream cipher is: ", cipherText)
    return cipherText


def decryptStreamCipher(cipherText, word):
    """takes in the encrypted text, and returns the plaintext"""
    key = buildkey(word)
    count = 0
    decryptText = ""

    for ch in cipherText:
        if count >= len(key): # this tells the function when the list has ended so it an start over
            count = 0
        if ch.isalpha(): # only encrypts letters

            stayInAlphabet = ord(ch) - key[count]
            count = count + 1

            if stayInAlphabet < ord('a'): # if it goes below a, add 26 to keep it a letter
                stayInAlphabet += 26
        else:
            stayInAlphabet = ord(ch)
        finalLetter = chr(stayInAlphabet)
        decryptText += finalLetter
    print("Your decrypted stream cipher is: ", decryptText)
    return cipherText


def main():

    key = 3 #the only number used in the simple cipher
    word = "doggy" #a medium sized key for the stream cipher
    plainText = "Hi mom! how are you?" # the plaintext that will be encrypted and decrypted this can be changed to test our program

    choice = input("Would you like to test the Simple cipher (1) or the stream cipher (2)")
    if choice == "2":
        decryptStreamCipher(plainText, word) #this input allows for easier testing
    # elif choice == "1":
    #     decryptSimpleCipher(encryptSimpleCipher(plainText, key), key)
    # else:
    #     print"I didn't get that"
    #     sys.exit()
    ########################################################################

main()
