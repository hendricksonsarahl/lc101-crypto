from helpers import alphabet_position, rotate_character
#import the helper functions from the helpers.py module to be used in our encryption

def encrypt(text, rot):
#Caesar cipher encryption function taking inputs 'text' and the degree of rotation
    jumbled_text = ""
    
    for letter in text:
        jumbled_text += rotate_character(letter, rot)
    return jumbled_text

def main():
#Where all the magic happens
    text = input("Enter text to be encrypted: ")
    rot = int(input("Enter the degree of jumblyness: "))
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()



    




