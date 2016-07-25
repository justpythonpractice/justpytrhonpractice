import datetime
import time
start = time.clock()
day1 = datetime.datetime(2015, 6, 29)
day2 = datetime.datetime(2015, 11, 24)
day2_minus_day1 = day2 - day1
print(day2_minus_day1)
print("---script was executing %s ms" % (time.clock() - start))