import xlrd
import datetime

book = xlrd.open_workbook("CALENDAR ABCD DAYS 2 (3) (1) (1) - Copy.xls")
sh = book.sheet_by_index(0)

current_time = datetime.datetime.now()
month = current_time.month
day = current_time.day

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
x=lastday
y=0
while(x<day):
	x+=7
	y+=2

daycol = 7-(x-day)
if(daycol>5):y+=2

wdays = sh.row_values(rowx=rowSt+1, start_colx=1, end_colx=6)
data = sh.row_values(rowx=rowSt+3+y, start_colx=1, end_colx=6)
dates = sh.row_values(rowx=rowSt+2+y, start_colx=1, end_colx=6)

for i in range(5):
    wday = wdays[i]
    result = data[i]
    date = dates [i]
    print(f'{wday},{date},{result}')

# +-----+------+-----+-------+-----+
# | mon | tues | wed | thurs | fri |
# +-----+------+-----+-------+-----+
# | 1/4 | 1/5  | 1/6 | 1/7   | 1/8 |
# +-----+------+-----+-------+-----+
# | a   | b    | c   | d     | e   |
# +-----+------+-----+-------+-----+
# |     |      |     |       |     |
# +-----+------+-----+-------+-----+



