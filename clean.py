import xlrd
import datetime

book = xlrd.open_workbook("CALENDAR ABCD DAYS 2 (3) (1) (1) - Copy.xls")
sh = book.sheet_by_index(0)


current_time = datetime.datetime.now()
month = current_time.month
#day = current_time.day

day = int(input("day:"))

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
	#print(f'{wday},{month}/{day}')
	result = sh.cell_value(rowx=rowSt+3,colx=daycol)
else:
	x=lastday
	y=0
	while(x<day):
		x+=7
		y+=2
	daycol = 7-(x-day)
	wday = sh.cell_value(rowx=rowSt+1,colx=daycol)
	#print(f'{wday},{month}/{day}')
	result = sh.cell_value(rowx=rowSt+3+y,colx=daycol)

final = '{0},{1}/{2}\n{3}'.format(wday, month, day,result)

print(final)