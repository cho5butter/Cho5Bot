from discord.ext import commands
import discord
import random
import asyncio
import os
import requests
import json
import re
from mcstatus import MinecraftServer
from datetime import date
import xml.etree.ElementTree as etree

#オリジナル関数
def uuid(userid):
    url= "https://api.mojang.com/users/profiles/minecraft/" + str(userid)
    res = requests.get(url)
    response = json.loads(res.text)
    return response["id"]

def getGeoCode(zipcode):
    url = 'http://geoapi.heartrails.com/api/json'
    payload = {'method':'searchByPostal'}
    payload['postal']= zipcode
    res = requests.get(url, params=payload).json()['response']['location'][0]
    loc = res['prefecture'] + res['prefecture'] + res['town']
    lat = res['y']
    lng = res['x']
    return (loc,lat,lng)

def getTimeSunMoon(lat, lng, time):
    year = time.year
    month = time.month
    day = time.day
    url = 'http://labs.bitmeister.jp/ohakon/api/?'
    payload = {'mode':'sun_moon_rise_set', 'year':year, 'month':month, 'day':day, 'lat':lat, 'lng':lng}
    response = requests.get(url, params=payload)

    data = etree.fromstring(response.content)

    sr = data[3][2].text
    ss = data[3][3].text
    mr = data[3][6].text
    ms = data[3][7].text
    ma = data[4].text

    return (sr, ss, mr, ms, ma)


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
    #await client.change_presence(game=discord.Game(name="FrePeServer"), status=discord.Status.online)
    await client.change_presence(activity=discord.Game(name="FrePeServer", type=1))

#コマンド関係
@client.command(description="鳴き声の後にランダムな猫画像が表示されます",
                brief="猫が出現")
async def neko(ctx):
    embed=discord.Embed(color=0xe9574c)
    embed.set_image(url="https://loremflickr.com/320/240/cat")
    await ctx.send('にゃーん', embed=embed)

@client.command()
async def inu(ctx):
    embed=discord.Embed(color=0xe9574c)
    embed.set_image(url="https://loremflickr.com/320/240/dog")
    await ctx.send('わん', embed=embed)

@client.command()
async def tukino(ctx):
    msg = ['マジキチおみくじスタート:rolling_eyes:','ドコドコ┗(^o^)┛','今日の運勢は:question:']
    result = '「「「「「**' + random.choice(['大大吉','大吉','凶後大吉','凶後吉','末大吉','末吉','向大吉','吉','中吉','小吉','小吉後吉','後吉','吉凶末分末大吉','吉凶不分末吉','吉凶相半','吉凶相交末吉','吉凶相央']) + '**」」」」」でした！'
    await ctx.send(msg[0])
    await asyncio.sleep(1)
    num = 0
    while num < 5:
        await ctx.send(msg[1])
        num += 1
        await asyncio.sleep(0.2)
    await asyncio.sleep(1)
    await ctx.send(msg[2])
    await asyncio.sleep(2)
    await ctx.send(result)

@client.command()
async def post(ctx, zipcode = "6308501"):
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
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=error)


@client.command()
async def mcuuid(ctx, id):
    try:
        msg = uuid(id)
        embed=discord.Embed(title=id, description=msg, color=0x0fa800)
        embed.set_author(name="UUID",icon_url="https://t1.rbxcdn.com/a8f882d102d3a03b4e88d6da5e696095")
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=error)

@client.command()
async def mcskin(ctx, id):
    try:
        mcuuid = uuid(id)
        url1 = "https://mine.ly/" + id + ".1"
        url2 = "https://minotar.net/avatar/" + mcuuid + ".png"
        url3 = "https://minecraft.jp/players/" + id
        embed = discord.Embed(title= id + 'のスキンの取得に成功しました', description=":hearts: 全体スキン↓\r" + url1 + "\r:diamonds: jmsプロフィール↓\r" + url3, color=0x55d761)
        embed.set_footer(text="uuid：" + mcuuid)
        embed.set_thumbnail(url=url2)
        embed.set_author(name=id,icon_url=url2)
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=error)

@client.command()
async def tenki(ctx, citycode = '290010'):
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
                await ctx.send('要求された地名の天気の取得は対応していないため、代わりに奈良市の天気を表示します')
                citycode = '290010'
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
        param = {"city": citycode}
        data = requests.get(url, params = param).json()
        embed=discord.Embed(title=':sunny: ' + data['title'], description='```' + data['description']['text'] + '```', color=0x53b2fc)
        for weather in data['forecasts']:
            embed.add_field(name=weather['dateLabel'], value=weather['telop'], inline=True)
        embed.set_thumbnail(url=data['forecasts'][0]['image']['url'])
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=error)

@client.command()
async def status(ctx, ip = "vanilla-tairiku.com"):
    try:
        server = MinecraftServer.lookup(ip)
        status = server.status()
        embed=discord.Embed(title=ip, color=0x0fa800)
        embed.set_author(name="サーバーの状態",icon_url="https://t1.rbxcdn.com/a8f882d102d3a03b4e88d6da5e696095")
        embed.add_field(name=":gear: バージョン", value=status.version.name, inline=True)
        embed.add_field(name=":zap: ping", value=status.latency, inline=True)
        embed.add_field(name=":video_game:   最大接続可能人数", value=status.players.max, inline=True)
        embed.add_field(name=":game_die:  プレイ人数", value=status.players.online, inline=True)
        if status.players.sample is not None:
            msg = ""
            counter = 1
            for player in status.players.sample:
                msg += str(counter) + '. ' + player.name + ' (' + player.id + ')\r'
                counter += 1
            embed.add_field(name=":grimacing: オンラインプレイヤー", value=msg, inline=True)

        else:
            embed.add_field(name=":grimacing: オンラインプレイヤー", value="現在プレイしている人はいません", inline=True)
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=error)

@client.command()
async def ping(ctx, ip = "vanilla-tairiku.com"):
    try:
        server = MinecraftServer.lookup(ip)
        status = server.status()
        msg = "応答時間は {0} msです".format(status.latency)
        embed=discord.Embed(title=ip, description=msg, color=0x0fa800)
        embed.set_author(name="ping",icon_url="https://t1.rbxcdn.com/a8f882d102d3a03b4e88d6da5e696095")
        await ctx.send(embed=embed)
    except:
        await ctx.send(embed=error)

@client.command()
async def sunmoon(ctx, zipcode = '6308213'):
    try:
        zip_pattern = re.compile('^[0-9]{7}$')
        if re.match(zip_pattern, zipcode):
            print('郵便番号が正規表現にマッチしました')
            #ハイフンを挿入
            insert_num = 3
            zipcode = '{0}{1}{2}'.format(zipcode[:insert_num], '-', zipcode[insert_num:])
            print(zipcode)
            #緯度経度を取得
            loc, lat, lng = getGeoCode(zipcode)
            sr, ss, mr, ms, ma = getTimeSunMoon(lat, lng, date.today())
            #画像を取得するための細工
            mai = int(float(ma))
            mai = '%02d' % mai
            embed=discord.Embed(title=":sunny: 日の出・日の入, 月の出・月の入の時刻 :full_moon:", description="各種情報を正常に取得できました", color=0x46ddd5)
            embed.set_thumbnail(url="http://www.geocities.jp/easyclub_choro/moon"+mai+".gif")
            embed.add_field(name=":round_pushpin: 場所情報", value="```情報取得場所の位置情報```", inline=False)
            embed.add_field(name="郵便番号", value=zipcode, inline=True)
            embed.add_field(name="住所", value=loc, inline=True)
            embed.add_field(name=":sun_with_face: 日の出・日の入", value="```日の出時刻と日の入り時刻```", inline=False)
            embed.add_field(name="日の出", value=sr, inline=True)
            embed.add_field(name="日の入り", value=ss, inline=True)
            embed.add_field(name=":first_quarter_moon_with_face: 月の出・月の入", value="```月の出時刻と月の入り時刻```", inline=False)
            embed.add_field(name="月の出", value=mr, inline=True)
            embed.add_field(name="月の入り", value=ms, inline=True)
            embed.add_field(name="正午月齢", value=ma, inline=True)
            await ctx.send(embed=embed)
        else:
            print('郵便番号が正規表現にマッチしませんでした')
            await ctx.send(embed=error)
    except:
        await ctx.send(embed=error)


#コマンド以外
@client.event
async def on_message(message):
    await client.process_commands(message)

    if client.user == message.author:
        return

    if message.content.startswith('ぬるぽ'):
        #await client.send_message(message.channel, message.author.mention + '\rヽ( ･∀･)ﾉ┌┛ｶﾞｯΣ(ﾉ`Д´)ﾉ')
        reply = f'{message.author.mention}\rヽ( ･∀･)ﾉ┌┛ｶﾞｯΣ(ﾉ`Д´)ﾉ'
        await message.channel.send(reply)
    elif message.content.startswith('ca!clean'):
        clean_flag = True
        while (clean_flag):
            msgs = [msg async for msg in client.logs_from(message.channel)]
            if len(msgs) > 1: # 1発言以下でdelete_messagesするとエラーになる
                await client.delete_messages(msgs)
            else:
                clean_flag = False
                await client.send_message(message.channel, 'ログの全削除が完了しました')
    else:
        return

#トークンは環境変数
client.run(os.environ.get("DISCORD_TOKEN"))
