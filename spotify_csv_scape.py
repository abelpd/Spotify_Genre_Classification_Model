import csv
import requests
from functions import daterange
from datetime import date, timedelta
from contextlib import closing


#https://spotifycharts.com/regional/global/daily/2017-01-01
#^^^^sample url of where I'll scrape
url = 'https://spotifycharts.com/regional/global/daily/'

begdate = date(2017,1,1)
enddate = date(2017,1,2)
testenddate = date(2019,5,1)

for single_date in daterange(begdate, enddate):
    date_url = url + str(single_date.strftime("%Y-%m-%d")) + '/download/'
    print (date_url)
    with closing(requests.get(date_url, stream=True)) as r:
        f = (line.decode('utf-8') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            # Handle each row here...
            print (row)