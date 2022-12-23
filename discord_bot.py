import os
import discord
import messages
import requests
import qrcode
from dotenv import load_dotenv
from discord.ext import commands
from pprint import pprint


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CMD_PREFIX = "/"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=CMD_PREFIX, intents=intents)

def get_invitation(discord_user):
    # Set the API endpoint URL
    invitation_url = os.getenv('DISCORD_CONTROLLER_INVITATION_URL')

    # Set the request payload
    payload = {
        "identifier": discord_user.id,
        "name": discord_user.name,
        "discriminator": discord_user.discriminator,
        "user": discord_user.name + "#" + discord_user.discriminator,
        "created_at": discord_user.created_at.isoformat()
    }

    # Set the authorization header with the bearer token
    headers = {
        "Authorization": os.getenv('DISCORD_CONTROLLER_TOKEN'),
        "Content-Type": "application/json",
    }

    # Make the POST request
    return requests.post(invitation_url, json=payload, headers=headers)


# Function to convert a string into a qr code
def create_qr_code(data: str, filename: str):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f'{bot.user} {messages.BOT_CONNECT_MSG}'
            f'{guild.name}(id: {guild.id})'
        )

@bot.event
async def on_message(message):
    print(message.channel.type)
    if message.author == bot.user:
        return
    # Direct message to bot
    elif message.channel.type == discord.ChannelType.private:
        if not message.content.startswith(CMD_PREFIX):
            await message.channel.send(messages.HELP_CMD_MSG)
    # Server message with mention to bot
    elif message.mentions and message.mentions[0] == bot.user:
        await message.author.send(messages.WELCOME_MSG)
        await message.author.send("--")
        await message.author.send(messages.HELP_CMD_MSG)
    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)

@bot.command(name='welcome', brief=messages.WELCOME_CMD_MSG_S, help=messages.WELCOME_CMD_MSG_L)
async def welcome(ctx):
    await ctx.send(messages.WELCOME_MSG)

@bot.command(name='info', brief=messages.INFO_CMD_MSG_S, help=messages.INFO_CMD_MSG_L)
async def info(ctx):
    print(f'User:               {format(ctx.message.author)}')
    print(f'User ID:            {format(ctx.message.author.id)}')
    print(f'User created at:    {format(ctx.message.author.created_at)}')
    print(f'User name:          {format(ctx.message.author.name)}')
    print(f'User discriminator: {format(ctx.message.author.discriminator)}')

    await ctx.send(f'User: {format(ctx.message.author)}')
    await ctx.send(f'User ID: {format(ctx.message.author.id)}')
    await ctx.send(f'User created at: {format(ctx.message.author.created_at)}')
    await ctx.send(f'User name: {format(ctx.message.author.name)}')
    await ctx.send(f'User discriminator: {format(ctx.message.author.discriminator)}')


email_desc = commands.parameter(default=messages.ISSUE_PARAM_EMAIL_DEFAULT, description=messages.ISSUE_PARAM_EMAIL_DESC)

@bot.command(name='issue', brief=messages.ISSUE_CMD_MSG_S, help=messages.ISSUE_CMD_MSG_L)
async def issue(ctx, email: str = email_desc):
    print("Email: {}".format(email))
    response = get_invitation(ctx.message.author)
    # Check the status code of the response

    if response.status_code == 200:
        # If the request is successful, print the response data
        invitation = response.json()['invitation']['invitationUrl']
        connectionId = response.json()['connectionId']
        create_qr_code(invitation, f'./resources/{connectionId}.png')
        
        print(response.json())
        await ctx.send(messages.ISSUE_MSG)
        await ctx.send(file=discord.File(f'./resources/{connectionId}.png'))
    else:
        # If the request is not successful, print the status code
        print("Request failed with status code:", response.status_code)



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

