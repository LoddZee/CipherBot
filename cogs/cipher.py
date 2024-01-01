### Cog for all cipher related commands

# IMPORTS #
import discord
from discord import app_commands
from discord.ext import commands

from cipher_helper import NON_DESTRUCTIVE_CIPHERS, DESTRUCTIVE_CIPHERS
from cipher_helper import format_encoded_message, format_decoded_message, format_random_encoding, sendEncodingError, sendDecodingError
from cipher_helper import EncodingError, DecodingError

# EVENT CLASS #
class Cipher(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None: # Initialise Cipher Cog
        self.bot = bot
        return
    
    @commands.Cog.listener()
    async def on_ready(self) -> None: # Bot is ready
        print("\tCipher")
        return
    
    @app_commands.command(name='encode', description='Encode a super secret message!')
    @app_commands.describe(method='Method used to encode!', message='Your message you need to encode!')
    async def encode_message(self, interaction: discord.Interaction, method: str, message: str) -> None: # Encode message!
        try:
            await interaction.response.send_message(format_encoded_message(message, method.lower()), ephemeral=True) 
        except EncodingError as e:
            await interaction.response.send_message(embed=sendEncodingError(e.message), ephemeral=True)
        return
    
    @app_commands.command(name='decode', description='Decode a super secret message!')
    @app_commands.describe(method='Method used to decode!', message='Your super secret message!')
    async def decode_message(self, interaction: discord.Interaction, method: str, message: str) -> None: # Decode message!
        try:
            await interaction.response.send_message(format_decoded_message(message, method.lower()), ephemeral=True)
        except DecodingError as e:
            await interaction.response.send_message(embed=sendDecodingError(e.message), ephemeral=True)
        return
    
    @encode_message.autocomplete('method') # Auto complete for the method of encoding
    async def method_encode_message_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        choices = [app_commands.Choice(name=cipher.capitalize(), value=cipher) for cipher in (NON_DESTRUCTIVE_CIPHERS + DESTRUCTIVE_CIPHERS)]
        return [choice for choice in choices if current.lower() in choice.name.lower()]
    
    @decode_message.autocomplete('method') # Auto complete for the method of decoding
    async def method_decode_message_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        choices = [app_commands.Choice(name=cipher.capitalize(), value=cipher) for cipher in (NON_DESTRUCTIVE_CIPHERS + DESTRUCTIVE_CIPHERS)]
        return [choice for choice in choices if current.lower() in choice.name.lower()]
    
    random_commands = app_commands.Group(name='random', description='for some random spiciness!') # This is a command group that makes commands like '/random encode' possible

    @random_commands.command(name='encode', description='Randomly encode a message! (Shown how it was encoded)')
    @app_commands.describe(message='Your super secret message!', steps='Number of encoding steps! (max of 30)')
    async def random_encode(self, interaction: discord.Interaction, message: str, steps: int = 5) -> None: # Randomly encode a message!
        if steps < 1: # Steps limiter
            await interaction.response.send_message(embed='Number of steps needs to be positive number!', ephemeral=True)
        elif steps > 30: # Max of 30 steps
            await interaction.response.send_message(embed='You can only have a maximum number of 30 steps!', ephemeral=True)
        
        try:
            await interaction.response.send_message(format_random_encoding(message, steps), ephemeral=True)
        except EncodingError as e:
            await interaction.response.send_message(embed=sendEncodingError(e.message), ephemeral=True)
        return

# RUN #
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Cipher(bot))