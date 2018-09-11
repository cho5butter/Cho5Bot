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

* 1. DiscordでAppを作成する
App（Bot）を作成し、Tokenの取得また、サーバーへの参加を行います

* 2. 環境を整える

pythonが実行できる環境で  
```
pip install -U discord.py
pip install -U requests
pip install -U mcstatus
```
を実行します  

* 3. 環境変数に以下を設定する
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

* 4. ファイルを実行する  
`python3 discordbot.py`  
でファイルを実行します

# コマンド一覧

| コマンド | 説明 |
|:-------:|:--------|
|c!neko|ボットが「にゃー」と鳴きます|
|c!inu|ボットが「わん」と鳴きます|
|c!tenki <citycode> or <prefecture>|<prefecture>（都道府県名）の位置の天気を取得します（代表都市）
例 `c!tenki 滋賀`  
但し、北海道は広いので、「稚内、網走、函館、札幌、旭川、釧路」のどれかの地名を指定ください（`c!tenki 北海道`)では取得できません  
また上記の地域以外でも地名コードを指定すると、その場所の天気を取得することができます  
地域コードはLivedoor天気に準じます（地名コードの見つけ方は少々複雑なため、自分で見つけられる方のみご利用ください）
例 `c!tenki 290020` => 奈良県風屋（`c!tenki 奈良`だと奈良市）
何も指定しなかった場合は奈良県奈良市の天気が表示されます|


# お問い合わせ
メールフォーム: <https://c5bt.net/contact>   
Twitter： <https://twitter.com/__cho__>
