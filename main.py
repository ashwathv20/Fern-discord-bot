import discord
from discord.ext import commands

#api tokens and bot token
from apikeys import *

intents = discord.Intents.all()
intents.members= True

client = commands.Bot(command_prefix = '$',intents=intents)
#client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("the bot ready")
    print("-------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hey, I am fern")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1124620362366320681)
    await channel.send("hey")

@client.event    
async def on_member_remove(member):
    channel = client.get_channel(1124620362366320681)
    await channel.send("f off")



client.run(bottoken)