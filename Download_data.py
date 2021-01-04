import time
import pandas as pd
import os
import requests
import zipfile,io
import datetime

os.chdir('E:\\trial')
os.getcwd()

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + datetime.timedelta(n)
        
def nse_bhavcopy(date):
    year = str(date.year)
    mon = date.strftime('%b').upper()
    d = str(date.strftime('%d'))
    url = 'https://www1.nseindia.com/content/historical/EQUITIES/' + year + '/' + mon  + '/cm' + d + mon + year + 'bhav.csv.zip' 
    a=requests.get(url)
    if(a.status_code==200):
        z = zipfile.ZipFile(io.BytesIO(a.content))
        z.extractall()
                
start_date = datetime.date(2020, 12, 26)
end_date = datetime.date.today()

for date in daterange(start_date, end_date):
    # Ignore Saturdays & Sundays
    if 5 <= date.weekday() <= 6:
        continue
    bhavcopy = nse_bhavcopy(date)
    time.sleep()

