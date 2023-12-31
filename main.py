
import discord
import os 
import requests
import json
import random
from discord.ext import commands

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
intents.members= True

client = commands.Bot(command_prefix = '$',intents=intents)
#client = commands.Bot(command_prefix="$")
client.remove_command("help")




@client.event
async def on_ready():
    print("the bot ready")
    print("-------------")
    await test()
    
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


@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel=ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("you are not in vc, join a vc first")

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("left the vc")
    else:
        await ctx.send("i am not in vc")


async def test():
    await client.add_cog(help_cog(client))
    await client.add_cog(music_cog(client))


client.run(os.getenv("btoken"))