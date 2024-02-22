try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    print('The pyperclip module is not installed. To copy the result to the clipboard, install it using: pip install pyperclip')
    # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Ciphere')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Function to toggle between encrypting and decrypting
def toggle_mode(current_mode):
    return 'decrypt' if current_mode == 'encrypt' else 'encrypt'

# Ask if the user wants to encrypt or decrypt at the start
print('Do you want to (e)ncrypt or (d)ecrypt?')
response = input('> ').lower()
if response.startswith('e') or response.startswith('d'):
    mode = 'encrypt' if response.startswith('e') else 'decrypt'
else:
    print('Invalid choice. Exiting...')
    exit()

# Let the user enter the key to use:
while True:  # Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey}) to use.')
    response = input('> ').upper()
    if response.isdecimal() and 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
    else:
        print('Invalid key. Please enter a valid numeric key.')

# Main loop for message input and encryption/decryption:
while True:
    print(f'Enter the message to {mode}.')
    message = input('> ')

    # Caesar cipher only works on uppercase letters:
    message = message.upper()

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    # Encrypt/decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            # Get the encrypted (or decrypted) number for this symbol.
            num = SYMBOLS.find(symbol)  # Get the number of the symbol.
            if mode == 'encrypt':
                num = (num + key) % len(SYMBOLS)
            elif mode == 'decrypt':
                num = (num - key) % len(SYMBOLS)

            # Add encrypted/decrypted number's symbol to translated:
            translated += SYMBOLS[num]
        else:
            # Just add the symbol without encrypting/decrypting:
            translated += symbol

    # Display the encrypted/decrypted string to the screen:
    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard.')
    except ImportError:
        print('To copy the result to the clipboard, install pyperclip using: pip install pyperclip')
        # Do nothing if pyperclip wasn't installed, list out the packages need to install
    except pyperclip.PyperclipException:
        print('Error copying to clipboard. Ensure your system supports clipboard operations.')

    # Ask if the user wants to toggle between encrypting and decrypting
    print(f'Do you want to toggle between (e)ncrypt and (d)ecrypt? (Press any other key to exit)')
    response = input('> ').lower()
    if response.startswith('e') or response.startswith('d'):
        mode = toggle_mode(mode)
        # Ask for the key value after toggling
        while True:  # Keep asking until the user enters a valid key.
            maxKey = len(SYMBOLS) - 1
            print(f'Please enter the key (0 to {maxKey}) to use.')
            response = input('> ').upper()
            if response.isdecimal() and 0 <= int(response) < len(SYMBOLS):
                key = int(response)
                break
            else:
                print('Invalid key. Please enter a valid numeric key.')
    else:
        break  # Exit the loop if the user does not want to toggle
