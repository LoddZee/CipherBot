### Cog mainly for holding any event that the bot runs into

# IMPORTS #
import discord
from discord.ext import commands

# EVENT CLASS #
class Events(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None: # Initialise Events Cog
        self.bot = bot
        return
    
    @commands.Cog.listener()
    async def on_ready(self) -> None: # Bot is ready
        print("\tEvents")
        activity = discord.Game(name="With Ciphers!") # You can change this to whatever BEFORE running bot
        await self.bot.change_presence(status=discord.Status.online, activity=activity) # Change Activity of Bot
        return
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild) -> None: # Bot has joined a server
        self.bot.tree.copy_global_to(guild=discord.Object(id=guild.id)) # Sync commands to bot
        await self.bot.tree.sync(guild=discord.Object(id=guild.id))
        return

# RUN #
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Events(bot))