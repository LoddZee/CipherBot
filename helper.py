### Helper functions for the bot

# IMPORTS #
import os
import shutil

import discord
from dotenv import load_dotenv

# SETUP #
load_dotenv()

# GENERAL FUNCTIONS #
def clear() -> None: # Clear Console
    print('\033c', end='')
    return

def getenv(secret: str) -> str: # Get Environment Variable
    return os.getenv(secret)

# LOGGER FUNCTIONS #
def clearLogger() -> None: # Clear everything in log file
    with open('discord.log', 'w') as log:
        log.write('')
    return

def saveLogger() -> None: # Backup log file
    try:
        shutil.copy('discord.log', 'discord-backup.log')
    except:
        print('\'discord.log\' not located...')
    return

# EMBED FUNCTIONS #
def sendError(description: str="Something went wrong... please try the command again") -> discord.Embed: # Premade error embed message
    errorMessage = discord.Embed(title="Error!", description=description, colour=0xFF0000)
    return errorMessage

def sendSuccess(description :str) -> discord.Embed: # Premade success embed message
    message = discord.Embed(title="Success!", description=description, colour=0x00FF00)
    return message
