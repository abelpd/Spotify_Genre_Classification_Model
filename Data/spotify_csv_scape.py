import csv
import requests
from datetime import date, timedelta
from contextlib import closing

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


#https://spotifycharts.com/regional/global/daily/2017-01-01
#^^^^sample url of where I'll scrape
url = 'https://spotifycharts.com/regional/global/daily/'
writeurl = r"C:\Users\abels\Desktop\spotify_scrape\data\Top_200_Spotify_Data\\"

begdate = date(2017,2,3)
enddate = date(2017,2,4)

for single_date in daterange(begdate, enddate):
    date_url = url + str(single_date.strftime("%Y-%m-%d")) + '/download/'
    print (date_url)

    with closing(requests.get(date_url, stream=True)) as r:
        r.encoding = r.apparent_encoding
        print (r.encoding)
        f = (line.decode() for line in r.iter_lines())
        #f = (line.decode('latin-1',errors='replace') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')

        for row in reader:
            row.append(str(single_date))
            with open(writeurl + str(single_date) + '.csv', 'a', newline='', encoding='utf_8') as w:
                #with open(writeurl + str(single_date) + '.csv', 'a', newline='', encoding='latin-1') as w:
                wr = csv.writer(w, quoting=csv.QUOTE_ALL)
                wr.writerow(row)