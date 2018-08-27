import discord
import random
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(game=discord.Game(name="FrePeServer"))

@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)
    else if message.content.startswith('/tukino'):
        msg = ['マジキチルーレットスタート:rolling_eyes:','ドコドコ┗(^o^)┛','今日の運勢は:question:']
        result = ['大大吉','大吉','凶後大吉','凶後吉','末大吉','末吉','向大吉','吉','中吉','小吉','小吉後吉','後吉','吉凶末分末大吉','吉凶不分末吉','吉凶相半','吉凶相交末吉','吉凶相央']
        rand = random.randrange(0,17)
        await client.send_message(message.channel, msg[0])
        sleep(1)
        for num in range(5):
            await client.send_message(message.channel, msg[1])
            sleep(0.2)
            break
        sleep(1)
        await client.send_message(message.channel, msg[2])
        sleep(2)
        await clinet.send_message(message.channel,result[rand])



client.run('NDgwNDQ1NTEyNTEyODMxNDg5.Dlp6ow.E1_2sSoBAYM4cqZywwGZZNl2EkM')
