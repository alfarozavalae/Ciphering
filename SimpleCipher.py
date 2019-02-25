#############################################################################################3
# some parts of this code were taken from the code shared with our class:
# owners are: Aleksander Krasnov and Elyor Tukhtasinov.

###############################################################################################


def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Decrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result
#check the above function

text = str(input("What is the text"))
s = 3
choice = input("Do you want to encrypt or decrypt? Type E to encrypt and D to decrypt")
if choice == "E":
    print("Cipher: " + encrypt(text,s) )
elif choice == "D":
    print("Cipher: " + decrypt(text,s))
