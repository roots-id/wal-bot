import os
import discord
import messages
import requests
import qrcode
import logging
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

def get_invitation(discord_user, email):
    # Set the API endpoint URL
    invitation_url = os.getenv('DISCORD_CONTROLLER_INVITATION_URL')

    # Set the request payload
    payload = {
        "identifier": discord_user.id,
        "name": discord_user.name,
        "discriminator": discord_user.discriminator,
        "user": discord_user.name + "#" + discord_user.discriminator,
        "created_at": discord_user.created_at.isoformat(),
        "email": email

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
    logging.info(f'message: {message.author} | {message.content}')
    print(message.channel.type)
    if message.author == bot.user:
        return
    # Direct message to bot
    elif message.channel.type == discord.ChannelType.private:
        if not message.content.startswith(CMD_PREFIX):
            await message.author.send(messages.WELCOME_MSG)
            await message.author.send("--")
            await message.author.send(messages.HELP_CMD_MSG)
    # Server message with mention to bot
    elif message.mentions and message.mentions[0] == bot.user:
        await message.author.send(messages.WELCOME_MSG)
        await message.author.send("--")
        await message.author.send(messages.HELP_CMD_MSG)
    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)

@bot.command(name='welcome', brief=messages.WELCOME_CMD_MSG_S, help=messages.WELCOME_CMD_MSG_L)
async def welcome(ctx):
    logging.info(f'cmd welcome: {ctx.message.author}')
    await ctx.send(messages.WELCOME_MSG)

@bot.command(name='info', brief=messages.INFO_CMD_MSG_S, help=messages.INFO_CMD_MSG_L)
async def info(ctx):    
    logging.info(f'cmd info: {ctx.message.author}')
    print(f'User:               {ctx.message.author}')
    print(f'User ID:            {ctx.message.author.id}')
    print(f'User created at:    {ctx.message.author.created_at}')
    print(f'User name:          {ctx.message.author.name}')
    print(f'User discriminator: {ctx.message.author.discriminator}')

    await ctx.send(f'User: {ctx.message.author}')
    await ctx.send(f'User ID: {ctx.message.author.id}')
    await ctx.send(f'User created at: {ctx.message.author.created_at}')
    await ctx.send(f'User name: {ctx.message.author.name}')
    await ctx.send(f'User discriminator: {ctx.message.author.discriminator}')


email_desc = commands.parameter(default=messages.ISSUE_PARAM_EMAIL_DEFAULT, description=messages.ISSUE_PARAM_EMAIL_DESC)

@bot.command(name='issue', brief=messages.ISSUE_CMD_MSG_S, help=messages.ISSUE_CMD_MSG_L)
async def issue(ctx, email: str = email_desc):
    logging.info(f'cmd issue: {ctx.message.author}')
    response = get_invitation(ctx.message.author, email)
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

@bot.command(name='issue_url', brief=messages.ISSUE_URL_CMD_MSG_S, help=messages.ISSUE_URL_CMD_MSG_L)
async def issue(ctx, email: str = email_desc):
    logging.info(f'cmd issue: {ctx.message.author}')
    response = get_invitation(ctx.message.author, email)
    # Check the status code of the response

    if response.status_code == 200:
        # If the request is successful, print the response data
        invitation = response.json()['invitation']['invitationUrl']
        
        print(response.json())
        await ctx.send(messages.ISSUE_URL_MSG)
        await ctx.send(invitation)
    else:
        # If the request is not successful, print the status code
        print("Request failed with status code:", response.status_code)

def create_log_file():
    log_directory = "./resources"
    log_file_path = f"{log_directory}/activity.log"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w"):
            pass  # create an empty file
        
    logging.basicConfig(filename='./resources/activity.log', level=logging.DEBUG, format='%(asctime)s | %(message)s')

""" 
To ask new joiners to get a credential?
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
 """
create_log_file()

bot.run(TOKEN)

