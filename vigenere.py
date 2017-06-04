from helpers import alphabet_position, rotate_character
#import the helper functions from the helpers.py module to be used in our encryption

   
def encrypt(text, keyword):
#Vigenere cipher encryption function taking inputs 'text' and keyword to be used for rotation

    jumbled_text = ""
    char_in_keyword = 0
    for i in range(len(text)):
        if text[i].isalpha():
            jumbled_text += rotate_character(text[i], alphabet_position(keyword[char_in_keyword % len(keyword)]))
            char_in_keyword += 1
        else:
            jumbled_text += text[i]
    return jumbled_text
   
def main():
#Where all the magic happens
    text = input("Enter the text you wish to encrypt: ")
    keyword = input("Enter the encryption key you wish to use: ")
    print(encrypt(text, keyword))

if __name__ == "__main__":
    main()


