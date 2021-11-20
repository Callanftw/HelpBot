import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

class Fun(commands.Cog):
    @commands.command(name='whos_joe', help='Don\'t ask who joe is!', brief='JOE MAMA')
    async def joe_cmd(self, ctx):
        await ctx.send(':weary:')

    @commands.command(name='exit', help='Shuts Down Bot. Requires Administrator.',
    brief = 'Admin Command' )
    @commands.has_permissions(administrator=True)
    async def exit_cmd(self, ctx):
        await ctx.send('Shutting down...')
        await asyncio.sleep(1)
        await ctx.send('Successfully disconnected.')
        await bot.close()
    
bot.add_cog(Fun(bot))
bot.run(TOKEN)
