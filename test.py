import discord, asyncio
import re, sys, os, csv, json, codecs, io


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

"""
with open("text.txt","r") as origin_file:
  stream_raw = origin_file.read()
  # ord(): the codepoint of the string
  str_num = (ord(str) for str in stream_raw)
  seed = 255
  str_con = "".join([chr(str^seed) for str in str_num])
  with open('text_encode.txt', 'w') as new_file:
    new_file.write(str_con)
"""

@client.event
async def on_message(message):
    print(message)
    f = codecs.open('reply_random.csv', 'r', "UTF-8", "ignore")
    dataReader = csv.reader(f)
    for row in dataReader:
        tex = re.search(row[2], str(message))
        if message.content.startswith(tex):
            await asyncio.sleep(row[0])
            post = bot.rand_w('res\\' + row[1] + '.txt')
            await client.send_message(message.channel, post)
            
    if message.content.startswith('こおりちゃんテスト'):
        counter = 0
        tmp = await client.send_message(message.channel, '了解しました……')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'あなたはこのチャンネルでは{}回発言しました。'.format(counter))
        
    elif message.content.startswith('こおりちゃん寝てる'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, '寝てないですよ！')

    elif message.content.startswith('こおり.*(ジャンプ|じゃんぷ)'):
        await asyncio.sleep(1)
        await client.send_message(message.channel, 'ぴょんぴょん')
        
    
token = open("to.ken").read()
client.run(token)
