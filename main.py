
import discord 
import cm_token
import random 
import time
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '.') 

@client.event 
async def on_ready():
    await client.change_presence(activity=discord.Game(name='.help - Kaybon#8555'))
    print('Bot is ready.')

@client.event
async def on_message(message):
    author = message.author 
    content = message.content 
    print('{}: {}'.format(author, content))
    channel = message.channel

    # ALL USERS COMMANDS #

    if message.content == ".help":
        embed = discord.Embed(title="**HELP ON BOT**", description="Some useful command", color=0x750075)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/603734865183244308/613455636658651147/badges2_72.png")
        embed.add_field(name="*.bot*", value="ㅤ", inline=False)
        embed.add_field(name="*.git*", value="ㅤ", inline=False)
        embed.add_field(name="*.roll*", value="ㅤ", inline=False)
        embed.add_field(name="*.pfc*", value="ㅤ", inline=False)
        embed.set_footer(text="@KAYBON#8555")
        await message.channel.send(content=None, embed=embed)

    elif message.content.startswith('.bot'):
        await channel.send('Made by Kaybon ©')

    elif message.content.startswith('.roll'):
        await channel.send(random.randint(1,101))

    elif message.content.startswith('.pfc'):
        await channel.send(random.choice(['Pierre', 'Feuille', 'Ciseaux']))

    elif message.content.startswith('.git'):
        await channel.send('https://github.com/kaybonn')

    # ADMIN COMMANDS #

    if message.content == ".admin":
        is_user_admin = False
        for i in message.author.roles:
            if i.permissions.administrator:
                is_user_admin = True
        if is_user_admin:
            await message.channel.send("TEST") 


client.run(cm_token.token)
