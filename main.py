import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$',intents=intents)
#client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("the bot ready")
    print("-------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hey, I am fern")


client.run('MTEyNDk4NjAxMjc3MTMwNzU5MA.G7O2_A.cQ4RwIpua1xmh0u-RkWv-PDJZloGN57Lxd8d0A')