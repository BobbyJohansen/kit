import time
import datetime
from datetime import timedelta,tzinfo
from pytz import timezone


chosen_time = datetime.datetime.strptime('4/22/2016 10:00:00', '%m/%d/%Y %H:%M:%S')
chosen_time = chosen_time.replace(tzinfo=timezone('US/Eastern'))

delta = (chosen_time - datetime.datetime.now(timezone('US/Eastern')))
deltastr = str(delta).replace(':', ' hours, ', 1).replace(':', ' minutes, ', 1) + ' seconds!'
print(deltastr)