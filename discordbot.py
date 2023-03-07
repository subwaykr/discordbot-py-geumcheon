from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.all()
intents.members = True

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
        
@client.event
async def on_member_join(member):
    fmt = '{0.mention}님! 여기는 서울특별시 금천구 입니다. 환영합니다!'
    channel = member.server.get_channel("1069624743944278179")
    await client.send_message(channel, fmt.format(member, member.server))
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("1078978489836896318")
    fmt = '{0.mention}님, 서울특별시 금천구 였습니다. 안녕히가십시오!'
    await client.send_message(channel, fmt.format(member, member.server))

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
