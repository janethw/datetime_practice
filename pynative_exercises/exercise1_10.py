# https://pynative.com/python-date-and-time-exercise/

from datetime import datetime, timedelta
import time
# pip install python-dateutil
from dateutil.relativedelta import *
import calendar

# 1. print current date and time
print(datetime.now())  # 2024-04-22 15:43:49.730309
print(datetime.now().time())  # 15:43:49.730320


# 2. convert string into datetime object
date_string = "Feb 25 2020 4:20pm"  # wanted output: 2020-02-25 16:20:00
date_as_dt_object = datetime.strptime(date_string,
                                      '%b %d %Y %I:%M%p')
print(date_as_dt_object, type(date_as_dt_object))


# 3. subtract a week (7 days) from a given date
given_date = datetime(2020, 2, 25)
print(given_date, type(given_date))
difference = timedelta(days=7)
print(difference)
new_date = given_date - difference
print(new_date.date(), type(new_date.date()))


# 4. Print a date in the format: Day_name Day_number Month_name Year
exercise_date = datetime(2020, 2, 25)  # output: Tuesday 25 February 2020
print(exercise_date, type(exercise_date))
formatted_date = datetime.strftime(exercise_date, '%A %d %B %Y')
alt_formatted_date = given_date.strftime('%A %d %B %Y')
print(formatted_date)
print(alt_formatted_date)


# 5. Find the day of the week of a given date
given_date2 = datetime(2020, 7, 26)  # output: Sunday
day_of_week_as_english_name = given_date2.strftime('%A')
print(day_of_week_as_english_name)
day_of_week_as_integer = given_date2.strftime('%w')
print(day_of_week_as_integer)  # where 0 is Sunday, 6 is Saturday

# 5b. Alternative using calendar module
import calendar

given_date = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)

# 6. Add a week (7 days) and 12 hours to a given date
# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)
# Expected output: 2020-03-29 22:00:00
date_diff = timedelta(days=7, hours=12)
later_date = given_date + date_diff
print(later_date)


# 7. Print current time in milliseconds
# Using datetime to get current time
current_time = datetime.now().time()
# However, here, need time module to get time in seconds since epoch, 1 Jan 1970
# import time
time_now = time.time()  # returns time in seconds, multiply by 1000 to get milliseconds
refined_time_now = int(round(time.time() * 1000))
print(time_now * 1000)
print(refined_time_now)


# 8. Convert datetime into string
given_date = datetime(2020, 2, 25)  # output: "2020-02-25 00:00:00"
date_as_str = datetime.strftime(given_date, '%Y-%m-%d %H:%M:%S')
print(date_as_str)


# 9. Calculate the date 4 months from the current date
# 2020-02-25
given_date = datetime(2020, 2, 25).date()  # output: 2020-06-25
print(given_date)
new_date = given_date + relativedelta(months=4)
print(new_date)


# 10. Calculate number of days between two given dates
# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)  # output: 205 days

date_diff = abs(date_1 - date_2)
print(date_diff.days)
