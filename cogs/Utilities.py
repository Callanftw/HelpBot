import asyncio
from discord.ext import commands

class Utilities(commands.Cog, description='Boring server commands that no one needs.'):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(name='exit', help='Shuts Down Bot. Requires Administrator.',
    brief = 'Shuts down the bot' )
    @commands.has_permissions(administrator=True)
    async def exit_cmd(self, ctx):
        await ctx.send('Shutting down...')
        await asyncio.sleep(1)
        await ctx.send('Successfully disconnected.')
        await self.bot.close()
    
    @commands.command(name='ping', help="Returns the bot's latency")
    async def ping_cmd(self, ctx):
        await ctx.send('Pong! {0}ms latency!'.format(round(self.bot.latency, 1000)))
        
def setup(bot):
    bot.add_cog(Utilities(bot))