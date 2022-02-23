import discord
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = None

with open('token.txt', 'r') as f:
    TOKEN = f.read()

intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}, MungLang Compiler v1.0')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def mung(ctx):
    await ctx.send('뭉랭을 컴파일합니다.')

bot.run(TOKEN)
