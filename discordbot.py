from discord.ext import commands
import discord
import random
import asyncio
import os

#変数
prefix = "c!"
desc = 'ちょこばた制作のオリジナルボットです'

#インスタンス生成
client = commands.Bot(command_prefix=prefix, description=desc)

#起動処理
@client.event
async def on_ready():
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="FrePeServer"))

#コマンド関係
@client.command(description="鳴き声の後にランダムな猫画像が表示されます",
                brief="猫が出現")
async def neko():
    await client.say('にゃーん')

@client.command()
async def inu():
    await client.say('わん')

@client.command()
async def tukino():
    msg = ['マジキチおみくじスタート:rolling_eyes:','ドコドコ┗(^o^)┛','今日の運勢は:question:']
    result = '「「「「「**' + random.choice(['大大吉','大吉','凶後大吉','凶後吉','末大吉','末吉','向大吉','吉','中吉','小吉','小吉後吉','後吉','吉凶末分末大吉','吉凶不分末吉','吉凶相半','吉凶相交末吉','吉凶相央']) + '**」」」」」でした！'
    await client.say(msg[0])
    await asyncio.sleep(1)
    num = 0
    while num < 5:
        await client.say(msg[1])
        num += 1
        await asyncio.sleep(0.2)
    await asyncio.sleep(1)
    await client.say(msg[2])
    await asyncio.sleep(2)
    await client.say(result)

#コマンド以外
@client.event
async def on_message(message):
    await client.process_commands(message)

    if client.user == message.author:
        return

#トークンは環境変数
client.run(os.environ.get("DISCORD_TOKEN"))
