import asyncio
from discord.ext import commands

class Fun(commands.Cog, description='Fun commands that serve no purpose, except to be fun!'):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='weary', help='*Requires An Argument*')
    async def joe_cmd(self, ctx, *, arg):
        try:  
            for x in range(0, int(arg)):
                await ctx.send(':weary:')
                await asyncio.sleep(1.01)
        except ValueError:
            print('value eroor')
            await ctx.send('That\'s not a number you idot')

def setup(bot):
    bot.add_cog(Fun(bot))