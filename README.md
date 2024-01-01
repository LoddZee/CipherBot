# CipherBot
A simple discord bot that can create ciphers!

## Table of Contents

* [Requirements](#requirements)
* [Features & Commands](#features--commands)

## Requirements
This bot is coded in python so you will need to install the `discord.py` library and the `dotenv` library.
```
# Install pip
npm install pip

# Install discord.py
pip install discord.py

# Install dotenv
pip install dotenv
```

## Features & Commands
This bot features 3 slash commands and a total of 8 ciphers to choose from:

## Commands
* [Encode](#encode)
* [Decode](#decode)
* [Random Encode](#random-encode)

## Ciphers
* Base64 > `/encode base64 MESSAGE`
* Atbash > `/encode atbash MESSAGE`
* Shift > `/encode shift 13 MESSAGE`
* Vigenere > `/encode vigenere SECRET MESSAGE`
* Rail Fence > `/encode railfence 3 MESSAGE`
* Binary > `/encode binary MESSAGE`
* Hexadecimal > `/encode hexadecimal MESSAGE`
* Morse > `/encode morse MESSAGE`

> Note: Any sort of KEY or VALUE with a cipher __**NEEDS**__ to be typed inside the `method` parameter.
> `Shift` requires a positive integer.
> `Vigenere` requires a string of alpha characters only (a-z, no numbers)
> `Rail Fence` requires a positive integer.

### Encode
`/encode [method] [message]`
Used to encode a message using a chosen cipher.

### Decode
`/decode [method] [message]`
Used to decode a message using a chosen cipher.

### Random Encode
`/random encode [message] <steps>`
Used to randomly encode a message with a certain amount of steps.
> Note: the steps parameter is optional and is defaulted to 5. Steps MUST be an integer between 1 and 30 inclusive.

## Contributing
You are welcome to contribute by submitting a Pull Request to the repository.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details