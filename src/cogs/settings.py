from discord.ext import commands
from util import updateChannel

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def setChannel(self, ctx, id=None):
        """Sets up the main counting channel."""
        if id is None:
            updateChannel(ctx.channel.id)
            return await ctx.send(f"Set current channel as the counting channel with channelId {ctx.channel.id}.")
        if not id[0].isnumeric():
            return await ctx.send("Please ensure you send a valid numeric id.")
        updateChannel(id)
        return await ctx.send(f"Successfully configured channelId to {id}.")

    # why not?       
    @commands.command()
    async def mit(self, ctx):
        await ctx.send("Is that referring to the Mental Institute of Technology?")
       
async def setup(bot):
    await bot.add_cog(Settings(bot))