import datetime as dt

print("What time did you check in? Use 24-hour HH:MM.")
time_in = input()
hour, minute = map(int, time_in.split(':'))
time_in = dt.timedelta(hours=hour, minutes=minute)
print("What time did you start lunch? Use HH:MM. Don't have a colon to skip lunch")
lunch_check_in = input()
lunch_check_out = ""
if (lunch_check_in.find(':') != -1):
    print("What time did you check out for lunch? Use HH:MM.")
    lunch_check_out = input()
    hour, minute = map(int, lunch_check_in.split(':'))
    lunch_check_in = dt.timedelta(hours=hour, minutes=minute)
    hour, minute = map(int, lunch_check_out.split(':'))
    lunch_check_out = dt.timedelta(hours=hour, minutes=minute)
    time_in += (lunch_check_out - lunch_check_in)
print("How long do you intend to be checked in for? Use HH:MM. Don't have a colon to default to 8 hours")
day_length = input()
if (day_length.find(':') != -1):
    hour, minute = map(int, day_length.split(':'))
    full_day = dt.timedelta(hours=hour, minutes=minute)
else:
    full_day = dt.timedelta(hours=8, minutes=0)
time_out = full_day + time_in
print("Check out at:", time_out)
