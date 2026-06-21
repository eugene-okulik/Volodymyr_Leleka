import datetime
my_time = 'Jan 15, 2023 - 12:05:33'
time = datetime.datetime.strptime(my_time,'%b %d, %Y - %X')
print(time)
print(time.strftime('%B'))
print(time.strftime('%d.%m.%Y, %H:%M'))
