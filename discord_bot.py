# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix='!', intents=intents)

#@client.event
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f'{bot.user} is connected to the following guilds:\n'
            f'{guild.name}(id: {guild.id})'
        )

#@client.event
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'yes':
        await message.channel.send("cool")
    print(message)
    print(message.content)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

""" 
To ask new joiners to get a credential?
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
 """
bot.run(TOKEN)