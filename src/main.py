import os
import discord 
import util

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="c!", intents=intents)
cogs = ["Settings"]

async def load_cogs():
    for cog in cogs:
        try:
            await bot.load_extension(f"cogs.{cog.lower()}")
            print(f"Loaded the {cog} cog successfully!")
        except Exception as e:
            print(f"WARNING! WARNING! YOUR CODE SUCKS BECAUSE {cog} FAILED TO LOAD! FIX NOW!!!!!")
            print(e)

@bot.event
async def on_ready():
    await load_cogs()
    print(f"Bot is logged in as {bot.user.name} via id {bot.user.id}!")

@bot.event
async def on_message(message):
    # prevent-us-from-hitting-the-rate-limit.wav
    if message.author == bot.user:
        return

    # use the prefix to avoid triggering the bot
    if message.content.startswith("c!"):
        return await bot.process_commands(message)

    # dynamically check if our message is from the data.json channel
    if message.channel.id == util.channelId:
        if util.updateCount(message.content):
            return # count successful
        else:
            await message.channel.send("Oh no! You broke the count. Shame...now we are back to the start.")

# we need to stop every command that does not exist from causing an exception in the console!
@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, CommandNotFound):
        return
    raise err

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))

