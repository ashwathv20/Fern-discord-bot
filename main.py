import discord
import os 
import requests
import json
import random
from discord.ext import commands


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
    url = "https://api.imgflip.com/get_memes"
    response = requests.request("GET",url)
    responseJSON = json.loads(response.text)


    #print(response.json())
    channel = client.get_channel(1124620362366320681)
    #await channel.send("hey")
    if(responseJSON['success'] == True):
        meme=random.choice(responseJSON['data']['memes'])
        await channel.send("Hello, <@" + str(member.id) + "> "+meme["url"])


@client.event    
async def on_member_remove(member):
    channel = client.get_channel(1124620362366320681)
    await channel.send("f off")



client.run(os.getenv("bottoken"))