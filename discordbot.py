from discord.ext import commands
import discord
import random
import asyncio
import os
import requests
import json
import re
from mcstatus import MinecraftServer

#オリジナル関数
def uuid(userid):
    url= "https://api.mojang.com/users/profiles/minecraft/" + str(userid)
    res = requests.get(url)
    response = json.loads(res.text)
    return response["id"]

#変数
prefix = "c!"
desc = 'ちょこばた制作のオリジナルボットです'
error = discord.Embed(title=":no_entry: エラー", description="実行に失敗しました\rコマンドの記述方法が間違っている可能性があります\r左メニューの「オリジナルbotの使い方」をもう一度ご確認ください", color=0xff0007)
error.set_footer(text="存在しないユーザー名や郵便番号を指定したときなどにも同様のエラーが発生します")

#インスタンス生成
client = commands.Bot(command_prefix=prefix, description=desc)

#起動処理
@client.event
async def on_ready():
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="FrePeServer"), status=discord.Status.dnd)

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

@client.command()
async def post(zipcode):
    try:
        zip_pattern = re.compile('^[0-9]{7}$')
        addressResult = ''
        if re.match(zip_pattern, zipcode):
            print('郵便番号が正規表現にマッチしました')
            url = "http://zipcloud.ibsnet.co.jp/api/search"
            param = {"zipcode": zipcode}
            res = requests.get(url, params=param)
            response = json.loads(res.text)
            address = response["results"][0]
            addressResult = address["address1"] + address["address2"] + address["address3"]
        else:
            print('郵便番号が正規表現にマッチしませんでした')
            addressResult = "郵便番号が不正です"

        embed=discord.Embed(title=zipcode, description=addressResult, color=0xff0007)
        embed.set_author(name="住所",icon_url="http://webest-net.com/wp-content/uploads/2015/12/unnamed-2.png")
        await client.say(embed=embed)
    except:
        await client.say(embed=error)


@client.command()
async def mcuuid(id):
    try:
        msg = uuid(id)
        embed=discord.Embed(title=id, description=msg, color=0x0fa800)
        embed.set_author(name="UUID",icon_url="https://t1.rbxcdn.com/a8f882d102d3a03b4e88d6da5e696095")
        await client.say(embed=embed)
    except:
        await client.say(embed=error)

@client.command()
async def mcskin(id):
    try:
        mcuuid = uuid(id)
        url1 = "https://mine.ly/" + id + ".1"
        url2 = "https://minotar.net/avatar/" + mcuuid + ".png"
        url3 = "https://minecraft.jp/players/" + id
        embed = discord.Embed(title= id + 'のスキンの取得に成功しました', description=":hearts: 全体スキン↓\r" + url1 + "\r:diamonds: jmsプロフィール↓\r" + url3, color=0x55d761)
        embed.set_footer(text="uuid：" + mcuuid)
        embed.set_thumbnail(url=url2)
        embed.set_author(name=id,icon_url=url2)
        await client.say(embed=embed)
    except:
        await client.say(embed=error)

@client.command()
async def tenki(citycode = '290010'):
    try:
        #都市コード正規表現
        location_pattern = re.compile('^[0-9]{6}$')
        if re.match(location_pattern, citycode):
            print('cityコードが入力されています')
        else:
            print('cityコードが入力されていないため変換を行います')
            f = open('code.json', 'r')
            json_dict = json.load(f)
            #引数１が辞書に存在するか確認する
            print(citycode)
            if citycode in json_dict:
                print('辞書のキーにマッチングしました')
                print('取得したCityコード： ' + json_dict[citycode])
                citycode = json_dict[citycode]
            else:
                print('辞書のキーにマッチングしませんでした')
                await client.say('要求された地名の天気の取得は対応していないため、代わりに奈良市の天気を表示します')
                citycode = '290010'
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
        param = {"city": citycode}
        data = requests.get(url, params = param).json()
        await client.say(data['title'])
        await client.say('--------------')
        await client.say(data['description']['text'])
        await client.say('--------------')
        for weather in data['forecasts']:
            await client.say(weather['dateLabel'] + ':' + weather['telop'])
    except:
        await client.say(embed=error)

@client.command()
async def status():
    server = MinecraftServer.lookup("cuw.aa0.netvolante.jp")
    status = server.status()
    msg = "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency)
    await client.say(msg)

#コマンド以外
@client.event
async def on_message(message):
    await client.process_commands(message)

    if client.user == message.author:
        return

    if message.content.startswith('ぬるぽ'):
        await client.send_message(message.channel, message.author.mention + '\rヽ( ･∀･)ﾉ┌┛ｶﾞｯΣ(ﾉ`Д´)ﾉ')

#トークンは環境変数
client.run(os.environ.get("DISCORD_TOKEN"))
