    # SOME IMPORTS #
import discord, time, datetime
import cm_token
import random 
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '.') 
bot = commands.Bot(command_prefix='.', description="description")

@client.event 
async def on_ready():
    await client.change_presence(activity=discord.Game(name='.help - Kaybon#8555'))
    print('Bot is ready.')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    author = message.author 
    content = message.content 
    print('{}: {}'.format(author, content))
    channel = message.channel

    # ALL USERS COMMANDS #

    if message.content == ".help":
        embed = discord.Embed(title="**Guides**", description="The prefix of the bot on this server is``.``.", color=0x750075, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/603734865183244308/613455636658651147/badges2_72.png")
        embed.add_field(name="*Fun(4)*", value="`.pfc`, `.roll`, `.coinflip`, `.lenny`", inline=False)
        embed.add_field(name="*Utility(2)*", value="`.bot`, `.git`", inline=False)
        embed.add_field(name="*Game(?)*", value="`Comming soon..`", inline=False)
        embed.set_footer(text="@KAYBON#8555")
        await author.send(content=None, embed=embed)

    # UTILITY COMMANDS

    elif message.content == ".bot":
        await channel.send('Made by Kaybon ©')

    elif message.content == ".git":
        await channel.send('https://github.com/kaybonn')

    # FUN COMMANDS #

    elif message.content == ".roll":
        await channel.send(random.randint(1,101))

    elif message.content == ".rate":
        x = random.randint(0, 10)
        await channel.send("I rate you {}/10".format(x))

    elif message.content == ".pfc":
        await channel.send(random.choice(['Pierre', 'Feuille', 'Ciseaux']))

    elif message.content == ".coinflip":
        await channel.send(random.choice(['Heads !', 'Tails !']))

    elif message.content == ".lenny":
        await channel.send(random.choice(['( ͡° ͜ʖ ͡°)', '(ツ)', '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)', 'ಠ_ಠ', '(☞ﾟ∀ﾟ)☞', '(¬‿¬)', 'ಠ╭╮ಠ', '♥‿♥', '◉_◉', '⚆ _ ⚆', '˙ ͜ʟ˙', 'ಠ⌣ಠ', 'ಠ‿↼', '¬_¬', 'ʘ‿ʘ', 'ಠOಠ', '◔̯◔', '°Д°', '^̮^', '╚(ಠ_ಠ)=┐', '[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]']))

    # GAME COMMANDS #

    elif message.content == ".startmc": 
        await channel.send('Soon..')

    # ADMIN COMMANDS #

    if message.content == ".admin":
        is_user_admin = False
        for i in message.author.roles:
            if i.permissions.administrator:
                is_user_admin = True
        if is_user_admin:
            await message.channel.send("TEST") 
        
    # kick command ( doesn't work, idk why ) #

@bot.command
async def kick(ctx, member : message.channel.guild.get_member, *, reason=None):
   await member.kick(member, reason=reason)
   await ctx.send(f"{ctx.message.author} kicked {member} for this reason: '{reason}'")

client.run(cm_token.token)
