import asyncio
import discord
import os
from discord import message
from discord.client import Client
from discord.ext.commands.core import check
from discord.ext.commands.help import DefaultHelpCommand
from dotenv import load_dotenv
from discord.ext import commands

checkifcommand = ''
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="-")

class Fun(commands.Cog):
    def __init__(self, client):
        bot = discord.client
        
    @bot.event
    async def on_ready():
        print(f'Logged on as {bot.user}!')



    @commands.command(name='whos_joe', help='Don\'t ask who joe is!', brief='JOE MAMA')
    async def Joe(ctx):
        
        await ctx.send(':weary:')

    @commands.command(name='exit', help='Shuts Down Bot. Requires Administrator.',
    brief = 'Admin Command' )
    
    @commands.has_permissions(administrator=True)

    
    async def _godie(ctx):

        await ctx.send('Shutting down...')
        await asyncio.sleep(1)
        await ctx.send('Successfully disconnected.')
        await bot.close()
    
    
bot.add_cog(Fun(bot))

bot.run(TOKEN)
