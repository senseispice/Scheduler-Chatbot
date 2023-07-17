import xlrd
import datetime

book = xlrd.open_workbook("CALENDAR ABCD DAYS 2 (3) (1) (1) - Copy.xls")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
#print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))

#month = 1
#rowSt = 74
current_time = datetime.datetime.now()
month = current_time.month

if(month==12):
	rowSt=56
else:
	rowSt = 14*(4+month)

# if(month=1):
# 	rowSt=71
# if(month=2):
# 	rowSt=85
# if(month=3):
# 	rowSt=99
# if(month=4):
# 	rowSt=113
# if(month=5):
# 	rowSt=127
# if(month=6)
# 	rowSt=141

findcol = True

while findcol:
	lst = sh.row_values(rowx=rowSt+2, start_colx=1, end_colx=None)
	#lst = sh.row(rowx=rowSt+2)
	onecol = 1
	for item in lst:
		if(item==1):
			findcol=False
			break
		else:
			onecol+=1

day = current_time.day

lastday = 8-onecol
if(day<lastday):
	daycol = (day-1)+onecol
	wday = sh.cell_value(rowx=rowSt+1,colx=daycol)
	print(f'{wday},{month}/{day}')
	print(sh.cell_value(rowx=rowSt+3,colx=daycol))
else:
	x=lastday
	y=0
	while(x<day):
		x+=7
		y+=2
	daycol = 7-(x-day)
	wday = sh.cell_value(rowx=rowSt+1,colx=daycol)
	print(f'{wday},{month}/{day}')
	print(sh.cell_value(rowx=rowSt+3+y,colx=daycol))














#for tries in range(7):
	#print(sh.cell_value(rowx=rowSt, colx=tries))



