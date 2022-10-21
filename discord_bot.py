# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

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
    print(message.channel.type)
    if message.author == bot.user:
        return
    # Direct message to bot
    elif message.channel.type == discord.ChannelType.private:
        await message.channel.send("I'm a bot, I don't respond to private messages")
    # Server message with mention to bot
    elif message.mentions and message.mentions[0] == bot.user:
        await message.author.send("Type /help for a list of commands")
    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine(ctx):
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