import discord
from discord.ext import commands

TOKEN = 'NzQxMTA4NTcyMjcxNjczMzU1.XyyxJA.9PID16Qg-MX3nYTJ3ZxEjoWgp60'

client = commands.Bot(command_prefix = 'K/')

@client.event
async def on_ready():
    print('Bot online and ready to run!')
    game = discord.Game("The newest lift. NLL 5E!")
    await client.change_presence(status=discord.Status.dnd, activity=game)

@client.command(pass_context=True)
async def EnterVC(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def LeaveVC(ctx):
    server = ctx.message.server
    VClient = client.voice_clients_in(server)
    await VClient.disconnect()


client.run(TOKEN)