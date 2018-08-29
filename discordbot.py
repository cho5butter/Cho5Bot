import discord
from discord.ext import commands
import random
import asyncio
from time import sleep
import os

BOT_PREFIX = ("?", "c!")
prefix = "c!"

client = commands.Bot(command_prefix = BOT_PREFIX)

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@client.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)
    elif message.content.startswith(prefix + 'tukino'):
        msg = ['マジキチおみくじスタート:rolling_eyes:','ドコドコ┗(^o^)┛','今日の運勢は:question:']
        result = '「「「「「**' + random.choice(['大大吉','大吉','凶後大吉','凶後吉','末大吉','末吉','向大吉','吉','中吉','小吉','小吉後吉','後吉','吉凶末分末大吉','吉凶不分末吉','吉凶相半','吉凶相交末吉','吉凶相央']) + '**」」」」」でした！'
        await client.send_message(message.channel, msg[0])
        await asyncio.sleep(1)
        num = 0
        while num < 5:
            await client.send_message(message.channel, msg[1])
            num += 1
            await asyncio.sleep(0.2)
        await asyncio.sleep(1)
        await client.send_message(message.channel, msg[2])
        await asyncio.sleep(2)
        await client.send_message(message.channel, result)

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(game=discord.Game(name="FrePeServer"))


client.run(os.environ.get("DISCORD_TOKEN"))
