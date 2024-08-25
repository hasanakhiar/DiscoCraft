import discord
from mcstatus import JavaServer
from discord.ext import commands

# Replace 'your-discord-bot-token' with your bot token
TOKEN = 'your-discord-bot-token'


SERVER_ADDRESS = 'SERVER_ADDRESS'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='minecraft')
async def server_status(ctx):
    try:
        server = JavaServer.lookup(SERVER_ADDRESS)
        status = server.status()

        await ctx.send(f"The server is online with {status.players.online} players. Ping: {status.latency} ms. (You can use !mine too ;)")
    except Exception as e:
        await ctx.send("The server is offline or unreachable right now... Please contact admin")
@bot.command(name='mine')
async def server_status(ctx):
    try:
        server = JavaServer.lookup(SERVER_ADDRESS)
        status = server.status()

        await ctx.send(f"The server is online with {status.players.online} players. Ping: {status.latency} ms")
    except Exception as e:
    	await ctx.send("The server is offline or unreachable right now... Please contact admin")
 
@bot.command(name='connect')
async def server_connect(ctx):
	await ctx.send("SERVER_ADDRESS")


bot.run(TOKEN)
