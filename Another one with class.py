# rhodese, detoren
#
# created on 9/22/2016
#
#

__author__ = 'heggens'
'''
This program implements three encryption algorithms:
Simple cipher, stream cipher, and a block cipher
'''

import io
import sys

def buildkey(key):
    """creates a string of intergers from the key. used in the stream cipher"""
    build = []
    for i in key:
        iter = keycode(i) # gets the value of the letter from keycode
        build.append(iter)

    return build

def keycode(key):
    """this function holds the dictionary that the stream cipher needs to operate"""
    code = {"a" : "c", "b" : "d", "c" : "e", "d" : "f", "e" : "g", "f" : "h", "g" : "e", "h" : "j", "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" :25 }
    return code[key]


def encryptSimpleCipher(plainText, key):
    """determines the encrypted string based on the plain text and the key"""
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + key
            if stayInAlphabet > ord('z'): # keeps the text from going above z
                stayInAlphabet -= 26
        else:
            stayInAlphabet = ord(ch)
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print "Your simple cipher is: ", cipherText
    return cipherText

def decryptSimpleCipher(cipherText, key):
    """decrypts the simple cipher string back into plain text"""
    cipherTexthere = ""
    key = -key
    cipherText = cipherText.lower()
    for ch in cipherText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + key #adds the number to the letter value
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26
        else:
            stayInAlphabet = ord(ch)
        finalLetter = chr(stayInAlphabet)
        cipherTexthere += finalLetter
    print "Your decrypted cipher is: ", cipherTexthere
    return cipherText

def encryptStreamCipher(plainText, word):
    """uses plaintext, and returns an encrypted string"""
    cipherText = ""
    plainText = plainText.lower()
    key = buildkey(word)
    count = 0

    for ch in plainText:
        if count >= len(key): #ensures that the function constantly uses the key
            count = 0
        if ch.isalpha():
            stayInAlphabet = ord(ch) + key[count]
            count = count + 1

            if stayInAlphabet > ord('z'): # keeps the encrypted letter from going above z
                stayInAlphabet -= 26
        else:
            stayInAlphabet = ord(ch)
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print "Your encrypted stream cipher is: ", cipherText
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
    print "Your decrypted stream cipher is: ", decryptText
    return cipherText


def main():

    key = 3 #the only number used in the simple cipher
    word = "doggy" #a medium sized key for the stream cipher
    plainText = "Hi mom! how are you?" # the plaintext that will be encrypted and decrypted this can be changed to test our program

    choice = raw_input("Would you like to test the Simple cipher (1) or the stream cipher (2)")
    if choice == "2":
        decryptStreamCipher(encryptStreamCipher(plainText, word), word) #this input allows for easier testing
    elif choice == "1":
        decryptSimpleCipher(encryptSimpleCipher(plainText, key), key)
    else:
        print "I didn't get that"
        sys.exit()
    ########################################################################
