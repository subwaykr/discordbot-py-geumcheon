from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == (f'금천구를 소개해줘'):
        await message.channel.send("금천구는 개발중인 로블록스 KR:RP형태의 서버입니다.")

    if message.content.startswith(f'안녕하세요!'):
        await message.channel.send('금천구에 오신걸 환영합니다!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
