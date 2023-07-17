
import discord
from discord.ext.commands import Bot
from discord import channel

import random
import xlrd
import datetime

token = "insert token here"
client = Bot(command_prefix="?")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mid 80s tunes | ?help"))

    i=0
    print("currently active:")
    for guild in client.guilds:  
        i+=1
        print(f'#{i}: working in {guild.name}, -- (id:{guild.id})')

    
@client.event
async def on_message(message):
     #print(message.author.name + " said, '" + message.content + "'")
     await client.process_commands(message)

     if "chromebook" in message.content.lower():
        await message.channel.send('you need help with that?')

     if("women" in message.content.lower() or "hate" in message.content.lower() or "based" in message.content.lower() or "pilled" in message.content.lower()):
        rad = random.randint(1,6)
        
#myid:461214732494307339
#dak:212592854713892864
     sys = random.randint(1,100)
     if(message.author.id==599270610190991374 and sys==20): await message.channel.send("I'm murdering this bot")


@client.command(name='day', help='get important details about today')
async def day(ctx, month:int=None, day:int=None):

    book = xlrd.open_workbook("calendars/CALENDAR ABCD DAYS 2 (3) (1) (1) - Copy.xls")
    sh = book.sheet_by_index(0)

    
    current_time = datetime.datetime.now()

    knuckles = [1,3,5,7,8,10,12]
    other = [4,6,9,11]

    futurect = 0

    if month == None: 
        month = current_time.month
    elif(day==None):
        day = current_time.day + month
        futurect = month
        month = current_time.month
        if(month in knuckles):
             if(day>31):
                 day-=31
                 month+=1
        elif(month in other):
            if(day>30):
                day-=30
                month+=1
        else:
            day-=28
            month+=1
      
    tmr = False
    if day == None:
        wkday = current_time.isoweekday()
        day = current_time.day
        if(current_time.hour>=16 or wkday>=6):
            day+=1
            tmr = True
    else: tmr=2

    #if(month>=9):month=-12
    #rowSt = 14*(4+month)

    if(month>12):month-=12

    if(month==12):
         rowSt=56
    else:
        rowSt = 14*(4+month)

    findcol = True

    while findcol:
        lst = sh.row_values(rowx=rowSt+2, start_colx=1, end_colx=None)
        onecol = 1
        for item in lst:
            if(item==1):
                findcol=False
                break
            else:
                onecol+=1

    lastday = 8-onecol
    if(day<lastday):
        daycol = (day-1)+onecol
        wday = sh.cell_value(rowx=rowSt+1,colx=daycol)
        result = sh.cell_value(rowx=rowSt+3,colx=daycol)
    else:
        x=lastday
        y=0
        while(x<day):
            x+=7
            y+=2
        daycol = 7-(x-day)
        wday = sh.cell_value(rowx=rowSt+1,colx=daycol)
        result = sh.cell_value(rowx=rowSt+3+y,colx=daycol)

    if(daycol>5):
        result = "it's the weekend u dope"
    
    spec = ""

    if(futurect>1):spec = f"**{futurect} days from now**"
    elif(futurect<0):spec = f"**{-1*futurect} days ago**"
    elif(tmr==True or futurect==1):spec = "**Tomorrow**"
    elif(tmr!=2):spec = '**Today**'

    

    final = '{0},{1}/{2}\n{3}'.format(wday, month, day, result)

    await ctx.send(f'{spec}\n{final}')

@client.command(name='week', help='get information about the upcoming or present week')
async def week(ctx, month:int=None, day:int=None):

    book = xlrd.open_workbook("calendars/CALENDAR ABCD DAYS 2 (3) (1) (1) - Copy.xls")
    sh = book.sheet_by_index(0)

    current_time = datetime.datetime.now()

    knuckles = [1,3,5,7,8,10,12]
    other = [4,6,9,11]

    if month == None: 
        month = current_time.month
    elif(day==None):
        day = current_time.day
        weekct = month
        month = current_time.month

        day = day+(7*weekct)

        if(month in knuckles):
            if(day>31):
                day-=31
                month+=1
        elif(month in other):
            if(day>30):
                day-=30
                month+=1
        else:
            day-=28
            month+=1

    if day == None:
        day = current_time.day

    if(month>=9):month-=12
    rowSt = 14*(4+month)

    findcol = True

    while findcol:
        lst = sh.row_values(rowx=rowSt+2, start_colx=1, end_colx=None)
        onecol = 1
        for item in lst:
            if(item==1):
                findcol=False
                break
            else:
                onecol+=1

    lastday = 8-onecol
    x=lastday
    y=0
    while(x<day):
        x+=7
        y+=2

    title = "This Week"
    daycol = 7-(x-day)
    if(daycol>5):
        y+=2
        title = "Upcoming Week"

    wdays = sh.row_values(rowx=rowSt+1, start_colx=1, end_colx=6)
    data = sh.row_values(rowx=rowSt+3+y, start_colx=1, end_colx=6)
    dates = sh.row_values(rowx=rowSt+2+y, start_colx=1, end_colx=6)

    for i in range(5):
        if not data[i]:
            if(dates[i]==1):
                dates[i]+=68
                rowSt = 14*(5+month)
                findcol = True
                while findcol:
                    lst = sh.row_values(rowx=rowSt+2, start_colx=1, end_colx=None)
                    onecol = 1
                    for item in lst:
                        if(item==1):
                            findcol=False
                            break
                        else:
                            onecol+=1
                for j in range(5-i):
                    data[i+j] = sh.cell_value(rowx=rowSt+3, colx=onecol+j)
                break
            else:
                count=0
                for value in dates:
                    if(value==1):break
                    count+=1
                day = dates[i]
                rowSt = 14*(3+month)
                lst = sh.row_values(rowx=rowSt+2, start_colx=1, end_colx=None)
                for m in range(len(lst)):
                    if(lst[m]==1):break
                x = 7-m
                while(x<day):
                    x+=7
                    y+=2
                daycol = int(7-(x-day))
                #newdata = sh.row_values(rowx=rowSt+3+y, start_colx=1, end_colx=count)
                for j in range(0,count):
                    data[i+j] = sh.cell_value(rowx=rowSt+3+y, colx=daycol+j)
                    dates[i+j]+=420
                break

    
    #topline = "+-----+------+-----+-------+-----+\n| mon | tues | wed | thurs | fri |"
    #middleline = f"\n'+-----+------+-----+-------+-----+\n| {dates[0]} | {dates[1]} | {dates[2]} | {dates[3]} | {dates[4]} |"
    #bottomline = f"\n'+-----+------+-----+-------+-----+\n| {data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]} |"
    
    #final = "".join((topline, middleline, bottomline))

    embed = discord.Embed(title=f"__**{title}:**__", color=0xb50520,timestamp= ctx.message.created_at)


    for i in range(5):
        if(dates[i]==69):
            dates[i]=1
            month+=1
        if(dates[i]>420):
            dates[i]-=420
            if(month<=1):newmonth = month+11
            else:newmonth = month-1
        elif(month<=0):newmonth=month+12
        else:newmonth=month
        embed.add_field(name=f'{wdays[i]}\n{newmonth}/{int(dates[i])}:', value=f'> {data[i]}',inline=False)

    await ctx.send(embed=embed)
    
client.run(token)