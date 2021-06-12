import asyncio,discord,os
from discord.ext import commands

game = discord.Game("!!명령어 입력")
bot = commands.Bot(command_prefix='!!',Status=discord.Status.online,activity=game,help_command=None)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".","?","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

@bot.event
async def on_ready():
    print("마이야히 마이야하")

if(True):
    bad = ['ㅅㅂ','시발','씨발',"시바", "새끼", "병신", "ㅅㄲ","ㅂㅅ","새1끼", "씨1발","병1신","시1발","시1바"] 
@bot.event
async def on_message(message): ##### remove bad words 
    message_contant=message.content 
    for i in bad: 
        if i in message_contant: 
            if message.author.dm_channel:
                await message.author.dm_channel.send("욕 좀 고마해라")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("욕 좀 고마해라")
            await message.channel.send('욕 필터링 ㅅㄱ') 
            await message.delete()

def password():
    a = "01011010100010011001100110010101100001101000000110111011010101101000100101111001100101010110100010011001100110100101011000101001010110111101010110101000100011111011100100111000110111010101101010100010110000110000111110011100011010000100010101111000001000001100111110010101100001110100000000110100010100101101010100001111010000111010011001001110101010000110000111110001100010101000001010101101100000000001110000111"
    b = 0
    c = ""
    d = int(len(a)/7)

    for i in range(0, d):
        b = 0
        for j in range(i*7, i*7+7):
            if(a[j] == "1"):
                b = b*2+1
            elif(a[j] == "0"):
                b = b*2
        c = c+alphabet[b-1]
    bot.run(c)
password()