import asyncio,discord,os
from discord.colour import Color
from discord.ext import commands

game = discord.Game("@@명령어 입력")
bot = commands.Bot(command_prefix='@@',Status=discord.Status.online,activity=game,help_command=None)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".","?","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

@bot.event
async def on_ready():
    print("마이야히 마이야하")

@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title=f"사용방법", descriotion=f"이진봇", Color=0xf3bb76)
    embed.add_field(name=f"-이진수를 십진수로",value=f"이진수_십진수 (이진수)", inline=False)
    embed.add_field(name=f"-십진수를 이진수로",value=f"십진수_이진수 (이진수)", inline=False)
    embed.add_field(name=f"-이진수를 영어로",value=f"이진수_영어 (이진수)", inline=False)
    embed.add_field(name=f"-영어를 이진수로",value=f"영어_이진수 (영어)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 이진수_십진수(ctx, text):
    a = text
    b = 0
    for i in range(0, len(a)):
        if(a[i] == "1" and b == 0):
            b = 1
        elif(a[i] == "1"):
            b = b*2+1
        elif(a[i] == "0"):
            b = b*2

    await ctx.send(b) 

@bot.command()
async def 십진수_이진수(ctx, text):
    b = int(text)
    a = 0
    c = ""

    while(b!=1):
        a += 1
        if(b%2 == 1):
            b = (b-1)/2
            c = "1" + c
        else:
            b = b/2
            c = "0" + c

    c = "1" + c
    await ctx.send(c)

@bot.command()
async def 이진수_영어(ctx, text):
    a = text
    b = 0
    c = ""
    d = int(len(a)/5)

    for i in range(0, d):
        b = 0
        for j in range(i*7, i*7+7):
            if(a[j] == "1"):
                b = b*2+1
            elif(a[j] == "0"):
                b = b*2
        c = c+alphabet[b-1]


    print(c)
    await ctx.send(c)

@bot.command()
async def 영어_이진수(ctx, *, text):
    p = []

    o = text

    for i in range(0, len(o)):
        for j in range(0, len(alphabet)):
            if(alphabet[j] == o[i]):
                p.append(j+1)

    a = 0
    c = ""
    result = ""

    for k in range(0, len(p)):
        b=p[k]
        a=0
        c=""
        while(b!=1):
            a += 1
            if(b%2 == 1):
                b = (b-1)/2
                c = "1" + c
            else:
                b = b/2
                c = "0" + c

        c = "1" + c
        if(len(c) != 5):
            for ii in range(0, 5-len(c)):
                c = "0" + c

        result = result+c
    await ctx.send(result)

def password():
    a = "01011010100010011001100110010101100001101001101110111100010110000110100110011011101001011010100010000001100110100101100000101000001110011000010110001000100110011011110100111000110111010101101010100001110011110000111110011100011001001010000011010010010100111110101110001011101000010100101000010100101110000010010111101010010111101000101000100000100010000010001111010111010010001101010000001000011111101010001000001"
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