# Cho5Bot(Discord)

[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg?longCache=true&style=flat)]()
[![Maintainability](https://api.codeclimate.com/v1/badges/f0c0914087d81e0922d7/maintainability)](https://codeclimate.com/github/cho5butter/AutomaticLoveReturn/maintainability)
[![Python](https://img.shields.io/badge/python-3.6.4-ff69b4.svg?longCache=true&style=flat)]()
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![Progress](https://img.shields.io/badge/progress-completion-green.svg?longCache=true&style=flat)]()


## 説明

ちょこぼっとは身内サーバー用に開発したDiscordBotです

## サーバーへ参加させる

[サーバーにBotを参加](https://discordapp.com/api/oauth2/authorize?client_id=480445512512831489&permissions=0&scope=bot)

## 使用上の注意

身内向けBotですので、例外処理が超絶適当です  
またエラー表示等の一部説明がこちらのサーバーに合わせてますので、表示が公開を想定していない箇所があります  

各種APIを使用していますので、過度に負担がかかる行為は控えて下さい  

## ローカルで実施する場合

* DiscordでAppを作成する

App（Bot）を作成し、Tokenの取得また、サーバーへの参加を行います

* 環境を整える

pythonが実行できる環境で  
```
pip install -U discord.py
pip install -U requests
pip install -U mcstatus
```
を実行します  

* 環境変数に以下を設定する

変数名：`DISCORD_TOKEN`  
この変数にDiscordTokenを設定します  

設定方法は使ってるshellや環境によっても異なります（以下一例）  
○herokuの場合  
`heroku config:set DISCORD_TOKEN="[取得したToken]"`  
○fishの場合  
```
cd ~/.config/fish
vim config.fish
```
で設定ファイルを開き、以下を追加します  
`set -x DISCORD_TOKEN "[取得したToken]"`  

* ファイルを実行する

`python3 discordbot.py`  
でファイルを実行します

# コマンド一覧

| コマンド | 説明 |
|:-------:|:--------|
|c!neko|ボットが「にゃー」と鳴きます|
|c!inu|ボットが「わん」と鳴きます|
|c!tenki [citycode] or [prefecture]|[prefecture]（都道府県名）又は[citycode]（都市コード[livedoor]）の位置の天気を取得します（代表都市|
|c!post [zipcode]|[zipcode]（郵便番号：ハイフン無しで記入）の場所の住所を調べます|
|c!sunmoon [zipcode]| [zipcode]（郵便番号：ハイフン無しで記入）の場所での本日の「日の出・日の入/月の出・月の入り・正午月齢」を調べられます|
|c!mcuuid [player]|[player]（PlayerID）のUUID（固有値）を取得します|
|c!mcskin [player]|[player]（PlayerID)のスキンをはじめ、様々な情報を取得します|
|c!ping [domain]|[domain]（サーバーアドレス）へピングを飛ばします|
|c!status [domain]|[domain]（サーバーアドレス）のプレイ人数、バージョン、接続者、応答時間などの様々な情報を確認できます|
|ぬるぽ|例のあれが帰ってきます|

# お問い合わせ
メールフォーム: [https://c5bt.net/contact]   
Twitter： [https://twitter.com/__cho__]
