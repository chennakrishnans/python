year=int (input ("Enter the year:"))
if (year%4==0 and year%100!=0):
    print ("The given year is leap year")
else:
    print ("The given is non leap year")
if year%4==0 and year%100!=0:
    prev_leap_year = year - 4
elif year % 400==0:
    prev_leap_year = year - 489
else:
    prev_leap_year = year - (year % 4)
print("leapyear:",prev_leap_year)
