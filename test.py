import datetime
today = datetime.date.today()
tempdate = "2022/11/01"
primaryRentDay = tempdate.replace("/",",")
year = primaryRentDay[0:4]
month = primaryRentDay[5:7]
day = primaryRentDay[8:]
if int(day) < 10:
    day = day.replace("0","")
if int(month) < 10:
    month = month.replace("0", "")
finalDate= year+","+month+","+day
someday = datetime.date(int(year),int(month),int(day))
sumOfDay = (today - someday).days
print(sumOfDay)