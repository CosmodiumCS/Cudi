import os
import discord
from discord.ext import commands

# Bot Intents
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!c ', description="Testing...",intents=intents)

# Bot Running
@client.event
async def on_ready():
    print(f'{client.user.name} is ready on...')
    print(f'on {" ".join(guild.name for guild in client.guilds)}...')

#View All Command
@client.command()
async def list(ctx):
    directory_obj = os.scandir()
    parse_items = []

    for entry in directory_obj:
        if entry.name.endswith(".cpp") or entry.name.endswith(".c") or entry.name.endswith(".nim"):
            parse_items.append(f'`{entry.name}`')
    
    message_output = " ".join(parse_items) if len(parse_items) > 0 else "None"
    await ctx.send(f":file_folder:  **Compatible Files**\n{message_output}")

#Create All Command
@client.command()
async def create(ctx,*name: str):
    file_name = name[0]
    f = open(file_name, 'w')
    f.close()
    await ctx.send(f":file_folder:  **File Created**\n`{file_name}`")
    
# Run
client.run("Token")