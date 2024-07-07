import os
import discord 
import json

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

load_dotenv()

with open("./data.json") as f:
    data = json.load(f)
channelId = data["channelId"]

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
    if message.author == bot.user:
        return

    if message.channel.id == channelId:
        await message.channel.send("This channel is defined.")

    await bot.process_commands(message)

# we need to stop every command that does not exist from causing an exception in the console!
@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, CommandNotFound):
        return
    raise err

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))

