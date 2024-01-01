#############################################
###               CipherBot               ###
###   A simple encoding/decoding discord  ###
###     for creating encoded messages     ###
###                                       ###
###          Created By: LoddZee          ###
###            Date: 19/12/2023           ###
#############################################

# Libraries to import:
# - discord
# - dotenv

# IMPORTS #
import os

### -> make sure you use `pip install discord` for these
import discord
from discord.ext import commands

import logging
import logging.handlers

from helper import getenv, clear, clearLogger, saveLogger

# SET UP #
saveLogger()
clearLogger()

logger = logging.getLogger('discord') # Setup logger
logger.setLevel(logging.INFO)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler( # Setup for logging handler
    filename='discord.log',
    encoding='utf-8',
    maxBytes=(32 * 1024 * 1024) # 32 Megabytes
)
handler.setFormatter(logging.Formatter('[{asctime}] [{levelname}] {name}: {message}', '%Y-%m-%d %H:%M:%S', style='{')) # Format for each log entry
logger.addHandler(handler)

# BOT CLASS #
class CipherBot(commands.Bot):
    
    def __init__(self) -> None: # Initialise Bot
        super().__init__( # Internal Bot Settings
            command_prefix='cipher!', # Don't worry about this. Prefixes won't be used
            intents=discord.Intents.all(),
            application_id=getenv('APP_ID'),
            help_command=None
        )
        self.synced = False
        self.logger = logger
        return
    
    async def on_connect(self) -> None: # Bot is online
        clear()
        return

    async def on_ready(self) -> None: # Bot is ready
        await self.wait_until_ready() # Do stuff before running commands
        print(f'{self.user} has connected to Discord.')
        
        # Attach cogs to bot
        print('Connecting Cogs:')
        if not self.synced:
            for guild in self.guilds:
                self.tree.copy_global_to(guild=guild) # Sync commands to every server
                await self.tree.sync(guild=discord.Object(id=guild.id))
        return
    
    async def setup_hook(self) -> None: # Update Commands
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        return
    
# RUN BOT #
bot = CipherBot()
try:
    bot.run(getenv('TOKEN'), log_handler=None) # Run bot :)
except KeyboardInterrupt: # If forced stop using keyboard inputs
    print('Bot is now offline!')