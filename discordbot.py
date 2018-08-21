import discord
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
client.run('NDgwNDQ1NTEyNTEyODMxNDg5.Dlp6ow.E1_2sSoBAYM4cqZywwGZZNl2EkM')
