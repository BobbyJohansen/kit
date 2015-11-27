import time
import datetime
from datetime import timedelta,tzinfo

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
            
            
EST = Zone(-5,False, 'EST')


now = datetime.datetime.now(EST).strftime('%m/%d/%Y %H:%M:%S')

pax = datetime.datetime.strptime('4/22/2015 10:00:00', '%m/%d/%Y %H:%M:%S')

difference = pax - now


print (difference)



