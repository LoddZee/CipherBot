### Where all encoding/decoding happens

# IMPORTS #
import discord

import random
import math
import base64

from helper import sendError

NON_DESTRUCTIVE_CIPHERS = ['base64', 'atbash', 'shift', 'vigenere', 'railfence']
DESTRUCTIVE_CIPHERS = ['binary', 'hexadecimal', 'morse']
RANDOM_KEYS = ['KEY', 'BOT', 'CIPHER', 'SECRET', 'PASSWORD', 'LODD', 'ABCXYZ', 'TIME', 'SPACE', 'PYTHON', 'DISCORD']

# Messaging
def format_encoded_message(message: str, method: str) -> str: # Format the encoded message output
    new_message = f'''```Decoded:
{message}``````Encoded:
{encoding(message, method)}```'''
    return new_message

def format_decoded_message(message: str, method: str) -> str: # Format the decoded message output
    new_message = f'''```Encoded:
{message}``````Decoded:
{decoding(message, method)}```'''
    return new_message

# Encoding Switch Case
def encoding(message: str, method: str) -> str: # Choose which method was inputted
    if method == 'base64': # Base64 Encode
        return b64_e(message)
    
    elif method == 'binary': # Binary Encode
        return binary_e(message)
    
    elif method == 'hexadecimal': # Hexadecimal Encode
        return hex_e(message)
    
    elif method == 'morse': # Morse Encode
        return morse_e(message)
    
    elif method == 'atbash': # Atbash Encode
        return atbash_e(message)
    
    elif method.startswith('shift'): # Shift Encode
        shift = None
        try:
            shift = int(method[5:]) # Get Shift Value
            return shift_e(message, shift)
        except Exception as e:
            if shift is None: # If there is no shift value...
                raise EncodingError(f'No shift value found... Please input a number after `Shift` in the method...\n\neg: `/encode Shift 12 Test!`')
            elif shift is not int: # If the shift value isn't a number...
                raise EncodingError(f'Incorrect shift value `{shift}`... Please input a number after `Shift` in the method...\n\neg: `/encode Shift 12 Test!`')
            raise EncodingError(f'Incorrect key value `{shift}`... Please try again!')
    
    elif method.startswith('vigenere'): # Vigenere Encode
        key = None
        try:
            key = method[8:].strip() # Get Vigenere Key
            return vigenere_e(message, key)
        except:
            if key is None or key == '': # If there is no key value...
                raise EncodingError(f'No key found... Please input a key after `Vigenere` in the method...\n\neg: `/encode Vigenere KEY Test!`')
            raise EncodingError(f'Incorrect key value `{key}`... Please try again!')
    
    elif method.startswith('railfence'): # Railfence Encode
        rails = None
        try:
            rails = int(method[9:]) # Get Rail Value
            return rail_fence_e(message, rails)
        except:
            if rails is None: # If there is no rails value...
                raise EncodingError(f'No rails value found... Please input a number after `Railfence` in the method...\n\neg: `/encode Railfence 3 Test!`')
            elif rails is not int: # If the rails value isn't a number...
                raise EncodingError(f'Incorrect rails value `{rails}`... Please input a number after `Railfence` in the method...\n\neg: `/encode Railfence 3 Test!`')
            raise EncodingError(f'Incorrect rails value `{rails}`... Please try again!')
        
    else: # Default / If inputted method doesn't exist
        raise EncodingError(f'Could not find encoding method `{rails}`... Please try again!')
    
# Decoding Switch Case
def decoding(message: str, method: str) -> str: # Choose which method was inputted
    if method == 'base64': # Base64 Decode
        return b64_d(message)
    
    elif method == 'binary': # Binary Decode
        return binary_d(message)
    
    elif method == 'hexadecimal': # Hexadecimal Decode
        return hex_d(message)
    
    elif method == 'morse': # Morse Decode
        return morse_d(message)
    
    elif method == 'atbash': # Atbash Decode
        return atbash_d(message)
    
    elif method.startswith('shift'): # Shift Decode
        shift = None
        try:
            shift = int(method[5:]) # Get Shift Value
            return shift_d(message, shift)
        except Exception as e:
            if shift is None: # If there is no shift value...
                raise DecodingError(f'No shift value found... Please input a number after `Shift` in the method...\n\neg: `/decode Shift 12 Test!`')
            elif shift is not int: # If the shift value isn't a number...
                raise DecodingError(f'Incorrect shift value `{shift}`... Please input a number after `Shift` in the method...\n\neg: `/decode Shift 12 Test!`')
            raise DecodingError(f'Incorrect key value `{shift}`... Please try again!')
    
    elif method.startswith('vigenere'): # Vigenere Decode
        key = None
        try:
            key = method[8:].strip() # Get Vigenere Key
            return vigenere_d(message, key)
        except:
            if key is None or key == '': # If there is no key value...
                raise DecodingError(f'No key found... Please input a key after `Vigenere` in the method...\n\neg: `/decode Vigenere KEY Test!`')
            raise DecodingError(f'Incorrect key value `{key}`... Please try again!')
    
    elif method.startswith('railfence'): # Railfence Encode
        rails = None
        try:
            rails = int(method[9:]) # Get Rail Value
            return rail_fence_d(message, rails)
        except:
            if rails is None: # If there is no rails value...
                raise DecodingError(f'No rails value found... Please input a number after `Railfence` in the method...\n\neg: `/decode Railfence 3 Test!`')
            elif rails is not int: # If the rails value isn't a number...
                raise DecodingError(f'Incorrect rails value `{rails}`... Please input a number after `Railfence` in the method...\n\neg: `/decode Railfence 3 Test!`')
            raise DecodingError(f'Incorrect rails value `{rails}`... Please try again!')
        
    else: # Default / If inputted method doesn't exist
        raise DecodingError(f'Could not find encoding method `{method}`... Please try again!')

# CIPHER METHODS #
# Base64
def b64_e(message: str) -> str: # Encode
    return base64.b64encode(message.encode()).decode() # Use base64 library

def b64_d(message: str) -> str: # Decode
    return base64.b64decode(message).decode() # Use base64 library.

# Binary
def binary_e(message: str) -> str: # Encode
    return ' '.join([bin(ord(char))[2:].zfill(8) for char in message]) # Goes through each letter, converts to ASCII value, converts to binary, fills out the 0's

def binary_d(message: str) -> str: # Decode
    binary_values = message.split()
    return ''.join([chr(int(binary, 2)) for binary in binary_values]) # Goes through each letter and converts back to character

# Hexadecimal
def hex_e(message: str) -> str: # Encode
    return ' '.join([hex(ord(char))[2:] for char in message]) # Goes through each letter, converts to ASCII value, converts to hexadecimal

def hex_d(message: str) -> str: # Decode
    hex_values = message.split()
    return ''.join([chr(int(hex, 16)) for hex in hex_values]) # Goes through each letter, converts back to character

# Morse Code
MORSE_CODE_DICT = { # Ascii to Morse Dictionary
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def morse_e(message) -> str: # Encode
    return ' '.join([MORSE_CODE_DICT[char.upper()] for char in message if (char.isalnum() or char == ' ')]) # Looks up each letter in morse code dictionary

def morse_d(message) -> str: # Decode
    morse_values = message.split(' ')
    return ''.join([list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(value)] for value in morse_values]) # Looks up the key for each morse code in message

# Atbash
def atbash_e(message) -> str: # Encode
    result = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            result += chr(ord('Z') - (ord(char.upper()) - ord('A')) + (0 if is_upper else 32)) # Convert to ASCII value, subtract from 'Z' value and subtract 'A' to get the inverse in the alphabet
        else:
            result += char
    return result

def atbash_d(message) -> str: # Decode
    return atbash_e(message) # Literally do the same as encoding lmao

# Shift
def shift_e(message: str, shift: int) -> str: # Encode
    result = ''.join([
        chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26
            + ord('A' if char.isupper() else 'a'))
        if char.isalpha() else char
        for char in message
    ]) # So this gets every letter, converts to ASCII, subtracts either 'A' or 'a' to get a simple number value, mod 26 incase of looping back around, and then add 'A' or 'a' to convert it back to a letter
    return result

def shift_d(message: str, shift: int) -> str: # Decode
    return shift_e(message, -shift) # Literally shift the same way as encoding but in the negative direction

# Vigenere
def vigenere_e(message: str, key: str) -> str: # Encode
    result = ""
    key_length = len(key)
    key = key.upper()
    key_drift = 0 # We have a key drift for any non-alpha characters so that the KEY can remain continuous throughout the message

    for i, char in enumerate(message):
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ((ord(char.upper()) + ord(key[(i - key_drift) % key_length].upper()) - 2 * ord('A')) % 26) + ord('A') # Honestly, magic. I can't explain this lmao
            result += chr(char_code + (0 if is_upper else 32))
        else:
            result += char
            key_drift += 1 if char == ' ' else 0

    return result

def vigenere_d(message: str, key: str) -> str: # Decode
    result = ""
    key_length = len(key)
    key = key.upper()
    key_drift = 0 # We have a key drift for any non-alpha characters so that the KEY can remain continuous throughout the message

    for i, char in enumerate(message):
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ((ord(char.upper()) - ord(key[(i - key_drift) % key_length].upper()) + 2 * ord('A')) % 26) + ord('A') # It's the same as encoding but inverse operations
            result += chr(char_code + (0 if is_upper else 32))
        else:
            result += char
            key_drift += 1 if char == ' ' else 0

    return result

# Rail Fence Cipher
def rail_fence_e(message: str, num_rails: int) -> str: # Encode
    rail_lines = ['' for _ in range(num_rails)]
    direction = 1
    rail_index = 0

    for char in message.replace(' ', ''): # Get each character
        rail_lines[rail_index] += char # Add it to designated line
        rail_index += direction # Continue in direction (up or down)

        if rail_index == num_rails - 1 or rail_index == 0: # If the index reachs either end
            direction = -direction # Invert direction
    
    return ' '.join(rail_lines)

def rail_fence_d(message: str, num_rails: int) -> str:
    direction = 1
    rail_index = 0

    rail_lines = message.split(' ') # Get each rail
    result = ''
    while len(rail_lines[rail_index]) > 0:
        result += rail_lines[rail_index][0] # Get the first letter of the rail
        rail_lines[rail_index] = rail_lines[rail_index][1:] # Pop out the first letter of the rail
        rail_index += direction # Continue in direction
        
        if rail_index == num_rails - 1 or rail_index == 0: # If the index reachs either end
            direction = -direction # Invert direction
    
    return result

# RANDOM ENCODING/DECODING #
def format_random_encoding(message: str, steps: int) -> str:
    original_message = message
    encoding_string = ''
    encoding_steps = []
    previous_step = None
    while len(encoding_steps) < steps: # Loop through number of steps
        random_step = random.choice(NON_DESTRUCTIVE_CIPHERS) # Choose a random Non Destructive Cipher. Destructive Ciphers can't be combined.
        if random_step == previous_step and previous_step is not None: # To make sure there are different steps along the way
            continue
        previous_step = random_step
        if random_step == 'shift': # Random shift value
            shift_val = str(random.randint(1, 25))
            encoding_string += f's{shift_val};'
            random_step += f' {shift_val}'
        elif random_step == 'vigenere': # Random vigenere key
            random_key = random.choice(RANDOM_KEYS)
            encoding_string += f'v{random_key};'
            random_step += f' {random_key}'
        elif random_step == 'railfence': # Random railfence value
            rail_val = str(random.randint(2, 5))
            encoding_string += f'r{rail_val};'
            random_step += f' {rail_val}'
        else:
            encoding_string += f'{random_step[0].lower()};' # Add to encoding string
        encoding_steps.append(random_step)
        message = encoding(message, random_step)

    encoding_steps_string = '\n'.join([f'{i + 1}. {e_step}' for i, e_step in enumerate(encoding_steps)])
    new_message = f'''```Message:
{original_message}``````Steps:
{encoding_steps_string}``````Output:
{message}``````Encoding String:
{encoding_string}```'''
    return new_message # Output the message

# OTHER #
# Encoding Error Embed
def sendEncodingError(description: str) -> discord.Embed: # Premade error embed message
    errorMessage = sendError(description)
    errorMessage.title = 'Encoding Error!'
    return errorMessage

# Encoding Error Embed
def sendDecodingError(description: str) -> discord.Embed: # Premade error embed message
    errorMessage = sendError(description)
    errorMessage.title = 'Decoding Error!'
    return errorMessage

# Encoding Error Class
class EncodingError(Exception):
    def __init__(self, message="Encoding Error...") -> None:
        self.message = message
        super().__init__(self.message)
    pass

# Decoding Error Class
class DecodingError(Exception):
    def __init__(self, message="Decoding Error...") -> None:
        self.message = message
        super().__init__(self.message)
    pass