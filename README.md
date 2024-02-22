# Caesar Cipher Encryptor/Decryptor 🔐

## Overview

This Python script implements a Caesar Cipher, a classic encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. The user can choose to either encrypt or decrypt a message, and the script supports toggling between encryption and decryption during runtime.

### What is the Caesar Cipher? 🕵️‍♂️

Its a Cryptography method used to communicate secretly. Imagine you have a secret code to talk to your friends, but you don't want others to understand it. The Caesar Cipher is like having a secret decoder ring. You and your friend decide on a number, let's say 3. Now, for each letter in your message, you move 3 places forward. So, if you write "A," it becomes "D," and "HELLO" becomes "KHOOR."

It's like a secret language only you and your friend understand because others might not know the secret number. This is a simple way people used to keep messages safe a long time ago!

Now, this Python script lets you use the Caesar Cipher to write secret messages or decode messages from your friends. It's like having your own secret code!

## Features

- Encrypt or decrypt messages using the Caesar Cipher algorithm.
- Toggle between encryption and decryption without restarting the script.
- Copy the result to the clipboard for easy sharing.

## Requirements

- Python 3.x
- (Optional) Pyperclip module for clipboard functionality. Install it using `pip install pyperclip`.

## Usage 🚀

1. Run the script using Python 3.
2. Choose whether to encrypt or decrypt the message.
3. Enter the key (shift value) to use for the Caesar Cipher.
4. Enter the message to be encrypted or decrypted.
5. View the result on the console and optionally copy it to the clipboard.
6. Choose to toggle between encryption and decryption for subsequent messages.

## Example

Encrypt a message:
```sh
Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 3
Enter the message to encrypt.
> HELLO
> KHOOR
Full encrypted text copied to clipboard.
Do you want to toggle between (e)ncrypt and (d)ecrypt? (Press any other key to exit)
> d
Please enter the key (0 to 25) to use.
> 3
Enter the message to decrypt.
> KHOOR
> HELLO
Full decrypted text copied to clipboard.
```

## Contribution 🤝

Contributions are welcome! If you'd like to enhance the script or fix any issues, please fork the repository and submit a pull request.
