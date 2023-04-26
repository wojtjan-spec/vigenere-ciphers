import sys
from math import log
from itertools import permutations

from vhelper import *

# dictionary
with open("eng-words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words

def check_all_words(string):
    all_words = 0
    count_of_eng = 0
    word_list = string.split()
    for word in word_list:
        all_words += 1
        if is_english_word(word) == True:
            count_of_eng += 1

    if (count_of_eng/all_words >= 0.8):
        return True
    else:
        return False

def decipher_vigenere(cipher_text, key):
    original_text = []
    for i in range(len(cipher_text)):
        if(cipher_text[i] == ' '):
            a = ord(' ')
        else:
            a = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            a += ord('A')
        original_text.append(chr(a))
    return("" . join(original_text))

def crack_vigenere_keys(input_cipher, hint_word):
    keys = []
    for i in range(len(input_cipher)-len(hint_word)):
        letters = []
        piece = input_cipher[i:i+len(hint_word)]
        decrypted_piece = decipher_vigenere(piece, hint_word)

        for letter in decrypted_piece:
            letters.append(letter)

        words = set()

        for length in range(1, len(letters) + 1):
            for subset in permutations(letters, length):
                word = ''.join(subset)
                words.add(word)

        for word in words:
            if (is_english_word(word) == True):
                if(len(word) <= len(hint_word)):
                    keys.append(word)

    return keys

def crack(input_cipher, keys, hint_word):
    final_texts = []
    for key in keys:
        keyword = key.replace(" ", "")
        stretched_key = stretch_key(input_cipher, keyword)
        cracked_text = decipher_vigenere(input_cipher, stretched_key)

        if check_all_words(cracked_text) == True:
            print("key: ", keyword)
            final_texts.append(cracked_text)

    return final_texts
            
def main():
    if len(sys.argv) != 4:
        print("------------------------------------------------------------------------------------------")
        print("[ERROR] Usage: python vcrack.py input_cipher.txt output_cracked.txt input_hint_word       ")
        print(" Please note: 1. The cipher cracking process is based on the hint word,                   ")
        print("                 that has to be present in the original message and at                    ")
        print("                 least as long as the key.                                                ")
        print("              2. The cipher is cracked based on the various key attempts and the          ")
        print("                 amount of fitting english words (at least 80 percent of the message).    ")
        print("------------------------------------------------------------------------------------------")
        return

    with open(sys.argv[1], 'r') as f:
        input_cipher = f.read()
    input_cipher = input_cipher.upper()

    input_hint_word = sys.argv[3]
    hint_word = input_hint_word.upper()

    possible_keys = crack_vigenere_keys(input_cipher, hint_word)
    cracked_texts = crack(input_cipher, possible_keys, hint_word)

    with open(sys.argv[2], 'w') as f:
        for cracked_text in cracked_texts:
            f.write(cracked_text.lower())
            f.write("\n")

if __name__ == '__main__':
    main()