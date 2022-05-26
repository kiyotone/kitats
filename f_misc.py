from datetime import date 
import datetime

def get_todate():
	today = date.today()
	day = str(today) + "-"
	z=0
	split_day = []

	for x in range(len(day)):
		if day[x] == "-":
			temp=""
			for y in range(z,x):
				temp=temp+day[y]
			split_day.append(temp)
			z=x+1

	return split_day

def total_days(lis):
	days_per_month=[31,28,31,30,31,30,31,31,30,31,30,31]
	yr=int(lis[0])
	mt=int(lis[1])
	dt=int(lis[2])
	leap_yr = yr/4
	days_in_month = 0
	days_in_year = yr * 365 + int(yr/4)

	if mt != 0:
		for x in range(0,mt-1):
			if x == 1 and yr % 4 == 0:
				days_in_month +=int(days_per_month[x])+1
			else:
				days_in_month += int(days_per_month[x])

	total = days_in_year+days_in_month+dt
	return total

def month_back(x):
	if x == 12:
		y = 1
	else:
		y=x-1
	return y



def leap_yrs(date1,date2):
	ly=0
	if int(total_days(date1)) < int(total_days(date2)):
		ate1=date1
		ate2=date2

	elif int(total_days(date1)) > int(total_days(date2)):
		ate1=date2
		ate2=date1
	else :
		return 0

	date2i = int(ate2[0])
	date1i = int(ate1[0])

	for x in range(date1i,date2i+1):
		if x % 4 == 0:
			ly+=1

	if int(ate1[1]) < 2:
		ly+=1

	if int(ate2[1]) > 2:
		ly+=1

	if int(ate1[1]) == 2:
		if int(ate1[2])=="29":
			ly+=1
	if int(ate1[2]) == 2:
		if int(ate2[2])=="29":
			ly+=1
	return ly

from datetime import date 
  
def str_age(born): 
	currentDate = datetime.datetime.now()
	age = []
	deadline= born
	deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
	daysLeft = currentDate - deadlineDate

	years = ((daysLeft.total_seconds())/(365.242*24*3600))
	yearsInt=int(years)
	age.append(yearsInt)

	months=(years-yearsInt)*12
	monthsInt=int(months)
	age.append(monthsInt)

	days=(months-monthsInt)*(365.242/12)
	daysInt=int(days)-1
	age.append(daysInt)

	hours = (days-daysInt)*24
	hoursInt=int(hours)

	minutes = (hours-hoursInt)*60
	minutesInt=int(minutes)

	seconds = (minutes-minutesInt)*60
	secondsInt =int(seconds)

	return age	      

def get_age(DOB):
	value=DOB[1]+"/"+DOB[2]+"/"+DOB[0]

	age = str_age(value)
	return age
