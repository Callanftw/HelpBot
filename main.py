import os
from discord.ext.commands import bot
import servercmds
from discord.ext.commands.errors import MissingRequiredArgument
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
global bot
bot = commands.Bot(command_prefix="-")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("You forgot to put something you idot") 

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


class Fun(commands.Cog):
    @commands.command(name='weary', help='*Requires An Argument*')
    async def joe_cmd(self, ctx, *, arg):
        try:  
            for x in range(0, int(arg)):
                await ctx.send(':weary:')
        except ValueError:
            print('value eroor')
            await ctx.send('That\'s not a number you idot')

bot.add_cog(servercmds.Utilities(bot))
bot.add_cog(Fun(bot))
bot.run(TOKEN)