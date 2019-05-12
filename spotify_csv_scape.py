import csv
import urllib2
from functions import daterange
from datetime import date, timedelta

#https://spotifycharts.com/regional/global/daily/2017-01-01
#^^^^sample url of where I'll scrape
url = 'https://spotifycharts.com/regional/global/daily/'

begdate = date(2017,1,1)
enddate = date(2019,5,1)

for single_date in daterange(begdate, enddate):
    print (single_date.strftime("%Y-%m-%d"))

