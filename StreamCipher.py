#############################################################################################
#  Acknowledgements
#  Jack Nelson -- https://github.com/jib1337/streamcipher/blob/master/streamcipher.py

#############################################################################################

from random import randint, seed

def encrypt(message):
        plntext = input('Enter message you would like to encrypt: ')
        seed(input('Enter your secret key. Make sure it is the same amount of characters as your text to encrypt '))

        encrypted = ''.join(chr(ord(c) ^ randint(0, 255)) for c in plntext)

        print('Your encrypted message is:', encrypted.encode('utf-8').hex() + '\n')
        return

def decrypt(message):

        seed(input('Enter your secret key. Make sure it is the same amount of characters as your text to encrypt '))
        try:
                print('Your decrypted message is:', ''.join(chr(ord(c) ^ randint(0, 255)) for c in enctext.decode('utf-8')) + '\n')
        except UnicodeDecodeError:
                print('Error: Error decoding hex. Please check input and try again.\n')

def printMenu():
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Exit\n')

print('Stream cipher')
message = False
printMenu()

while True:
        choice = input('What do you want to do: ')

        if choice == '1':
                encrypt(message)
                printMenu()
        elif choice == '2':
                decrypt(message)
                printMenu()
        elif choice == '3':
                if message == False:
                        message = True
                else:
                        message = False
                print('File Mode:', message, '\n')
                break
        else:
                continue
