import csv
import requests
from datetime import date, timedelta
from contextlib import closing

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


begdate = date(2017,1,1)
enddate = date(2019,5,1)


for single_date in daterange(begdate, enddate):
    print (single_date)

x = daterange(begdate, enddate)
print (type(x))