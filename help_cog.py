import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.help_message = """
```
General commands:
$help - displays all the commands
$p <song name -keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused
$q - displays the current music queue
$skip/$nah - skips the current song being played
$clear/$clear - Stops the music and clears the queue
$dc/$foff - Disconnected the bot from the voice channel
$pause - pauses the current song being played or resumes if already paused
$resume - resumes playing the current song
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)