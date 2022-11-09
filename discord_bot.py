# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from pprint import pprint


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
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
    #elif message.channel.type == discord.ChannelType.private:
    #    await message.channel.send("I'm a bot, I don't respond to private messages")
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

@bot.command(name='info', help='Responds with a qr code')
async def info(ctx):
    print(ctx.message.author)
    print(ctx.message.author.id)
    print(ctx.message.author.created_at)
    print(ctx.message.author.display_name)
    print(ctx.message.author.name)
    print(ctx.message.author.discriminator)
    print(bot.get_user(ctx.message.author.id).email)

    await ctx.send(file=discord.File('./resources/test_qr_code.jpg'))

@bot.command(name='invite', help='Responds with a qr code')
async def invite(ctx):
    await ctx.send(file=discord.File('./resources/test_qr_code.jpg'))

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