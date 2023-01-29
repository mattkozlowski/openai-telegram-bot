# OPEN AI - GPT3 CHAT INSIDE YOU TELEGRAM

## TELEGRAM BOT SETUP

1. Find BotFather on Telegram search - type @BotFather

2. In the conversation type /newbot and name it ex. GPT3_bot and type a username for your bot ex. MyName_GPT3_Bot

3. Now you can get a token to access HTTP API - just copy it.



## OPEN API -GETTING ACCESS KEY
Browse to https://beta.openai.com/account/api-keys and create a new secret key and copy it.

## CHANGE A CODE USING THESE ACCESS keys
Open server.py in text editor and insert your api keys in the right places:
 - line 6 - open api key between " "
 - line 8 - telegram token between " "

## RUN server.py on your server
    python3 server.py

## TRY CHATTING WITH GPT3

    /hello


    /ask write a tweet about why is important to have work-life-balance
