import sys
from vhelper import *

def decipher_vigenere(cipher_text, key):
    original_text = []
    for i in range(len(cipher_text)):
        a = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        a += ord('A')
        original_text.append(chr(a))
    return("" . join(original_text))

def main():

    if len(sys.argv) != 4:
        print("------------------------------------------------------------------------------------------")
        print("[ERROR] Usage: python vdecrypt.py input_cipher.txt output_original.txt input_key_string   ")
        print(" Please note: the decryption of the cipher is always in (ALL)CAPS.                        ")
        print("------------------------------------------------------------------------------------------")
        return

    with open(sys.argv[1], 'r') as f:
        input_cipher = f.read()

    input_key_string = sys.argv[3]
    input_key_string = input_key_string.upper()

    key = stretch_key(input_cipher, input_key_string)
    output_original = decipher_vigenere(input_cipher, key)

    with open(sys.argv[2], 'w') as f:
        f.write(output_original)

if __name__ == '__main__':
    main()