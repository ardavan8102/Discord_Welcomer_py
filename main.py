# ---------------------------------------------------  αυтнσя : αя∂αναη81  -------------------------------------------------------------------- #
import discord 
from discord import Intents
from discord.ext import commands
from asyncio import *
from colorama import Fore,init
init()


# Bot Configs

class CONFIG:
    TOKEN = '' # Bot Token
    PREFIX = '' # Bot Prefix

# Bot Variable

client = commands.Bot(command_prefix=CONFIG.PREFIX, intents=Intents.all())


# When Bot Comes Online :

def onmsg():
    print(Fore.GREEN+'\n >> BOT IS ONLINE'+Fore.CYAN+'\n >> Logged As {0.user}'.format(client))


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Test python Bot !"))
    onmsg()


# Greetings For New Members

@client.event
async def on_member_join(member):
    # change channel_id to your id (example = 12345456767)
    channel = client.get_channel(channel_id)
    created_at = member.created_at.strftime("%b %d, %Y")
    embed=discord.Embed(
        title='Welcomer Bot',
        description=f'{member.mention},\n**Welcome To Server!**',
        colour = 0xFFFF00
    )
    embed.add_field(name='**Joined Discord : **', value=f'``'+created_at+f'``', inline=False)
    embed.set_footer(text='Author : Ardavan81')
    embed.set_thumbnail(url=f'{member.avatar_url}')
    await channel.send(embed=embed)




# Make Bot Run

client.run(CONFIG.TOKEN)


# ---------------------------------------------------  αυтнσя : αя∂αναη81  -------------------------------------------------------------------- #