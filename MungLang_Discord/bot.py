import discord
import sys
import os

from discord.ext.commands import Bot
from discord.ext import commands

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + '/MungLang_Python')

import compiler

TOKEN = None

with open('token.txt', 'r') as f:
    TOKEN = f.read()

intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)
compiler = compiler.MungLanguage()

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}, MungLang Compiler v1.0')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def mung(ctx, *, code:str = None):
    if code is None:
        await ctx.send('코드를 입력해주세요.')
        return

    await ctx.send('뭉랭을 컴파일합니다.')

    try:
        code = code.split('\n')[1:-1]

        result = compiler.compile(code)
        result_string = '```\n' + '\n'.join(result) + '\n```'

        await ctx.send(result_string)

    except SyntaxError as e:
        await ctx.send('```\n' + e.msg + '\n```')


bot.run(TOKEN)
