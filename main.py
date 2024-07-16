
import asyncio
import discord
from discord.ext import commands
import time
from time import sleep
import os
import B
from discord import Client
from discord import Intents


intents = discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents-intents) 
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    #print(Client.user.name)
    #print(client.user.id)
    print('-'*20)
    await client.change_presence(activity=discord.Game(name='Deleting'))
    channel = client.get_channel(848085061601198090)
    #while True:
       # pass
        #await channel.purge(limit=4)
 
@client.command()
async def clear(ctx, number):
    num = int(number) #Converting the
    await ctx.channel.purge(limit=num) 

@client.command(pass_context = True)
async def thoda(ctx):
    while True:
        await ctx.channel.purge(limit=4)
        await asyncio.sleep(1)
        await ctx.send('<@904064220306493520>')
B.b()
my_secret = os.environ['TOKEN']
client.run(os.getenv(my_secret))
