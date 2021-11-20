import os
from discord.ext.commands import bot
from discord.ext.commands.errors import MissingRequiredArgument
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="-")
bot.remove_command('help')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Missing Required Argument") 

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

if __name__ == "__main__":
    bot.load_extension("cogs.Utilities")
    bot.load_extension("cogs.Fun")
    bot.load_extension("cogs.Help")
    bot.run(TOKEN)
