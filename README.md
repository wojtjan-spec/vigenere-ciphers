# Vigenere Cipher Programs
## Introduction

This project contains three Python programs that demonstrate the implementation of the Vigenere Cipher. The Vigenere Cipher is a polyalphabetic substitution cipher that is used for encrypting and decrypting plain text messages.Programs

## Programs
### vencrypt.py

This program implements encryption using the Vigenere Cipher. It takes three command-line arguments: the filename of a file containing the plaintext, the name of a file where the ciphertext will be written, and the key to be used for encryption. The program creates a file, with the appropriate name, containing the ciphertext. The program does not print anything to the screen.

Usage:
> python vdecrypt.py ciphertext.txt plaintext.txt key

### vdecrypt.py
This program implements decryption using the Vigenere Cipher. It takes three command-line arguments: the filename of a file containing the ciphertext, the name of a file where the plaintext will be written, and the key to be used for decryption. The program creates a file, with the appropriate name, containing the plaintext. The program does not print anything to the screen.

Usage:
> python vdecrypt.py ciphertext.txt plaintext.txt key

### vcrack.py
This program cracks the Vigenere Cipher by discovering the key from the ciphertext, without seeing the corresponding plaintext. In order to accomplish this, the program uses a hint word: a single word which is known to be in the plaintext, and which is at least as long as the key. The program takes two command-line arguments: the name of the file containing the ciphertext, and the hint word. The program prints the key on the screen.

Usage:
> python vcrack.py ciphertext.txt hintword

## Assumptions

These are some assumptions about the plaintext and the key:

1. Each word in the plaintext must be a word in the English language.
2. The plaintext must be sufficiently long, containing at least 100 words.
3. Each word in the plaintext must contain only lowercase, alphabetic characters.
4. The key must contain only lowercase, alphabetic characters.
5. The key must contain no spaces; it is a single word.
6. Spaces will almost certainly be included in the plaintext, but the spaces should NOT be encrypted and they will appear as-is, in the ciphertext.

## Conclusion

These programs demonstrate how the Vigenere Cipher can be used to encrypt and decrypt plain text messages. The programs can be run from the command line with appropriate arguments, and can be used for educational or practical purposes.

## Sources

1. https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf
2. https://inventwithpython.com/hacking/chapter21.html
3. https://rumkin.com/tools/cipher/vigenere/