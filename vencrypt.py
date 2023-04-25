import sys
from vhelper import *

def cipher_vigenere(input_text, key):
    cipher_text = []
    for i in range(len(input_text)):
        a = (ord(input_text[i]) +
             ord(key[i])) % 26
        a += ord('A')
        cipher_text.append(chr(a))
    return("" . join(cipher_text))
     
def main():

    if len(sys.argv) != 4:
        print("------------------------------------------------------------------------------------------")
        print("[ERROR] Usage: python vencrypt.py input_text.txt output_cipher.txt input_key_string       ")
        print(" Please note: the encryption works only if both the message and the key are in (ALL)CAPS. ")
        print("------------------------------------------------------------------------------------------")
        return

    with open(sys.argv[1], 'r') as f:
        input_text = f.read()
    input_text = input_text.upper()

    input_key_string = sys.argv[3]
    input_key_string = input_key_string.upper()

    key = stretch_key(input_text, input_key_string)
    output_cipher = cipher_vigenere(input_text, key)

    with open(sys.argv[2], 'w') as f:
        f.write(output_cipher)

if __name__ == '__main__':
    main()