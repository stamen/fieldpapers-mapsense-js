#! /usr/bin/env python

import csv
import time

ndigits = 4 # how many digits to round lat/lon coordinates. 4 is about 10m precision

head = None
doc = csv.reader(open('boxes.csv'), dialect='excel', delimiter='\t')
for row in doc:
    if not head:
        head = row
        newrow = ['atlas_id','timestamp','provider']
        newrow.extend(['lat','lon','width','height'])
        print ','.join(newrow)
    else:
        west = round(float(row[head.index('west')]),ndigits)
        south = round(float(row[head.index('south')]),ndigits)
        east = round(float(row[head.index('east')]),ndigits)
        north = round(float(row[head.index('north')]),ndigits)
        lat = round((north + south) / 2,ndigits)
        height = round(north - south,ndigits)
        lon = round((east + west) / 2,ndigits)
        width = round(east - west,ndigits)

        if north > 90 or north < -90 or west > 180 or west < -180:
            continue
        if south > 90 or south < -90 or east > 180 or east < -180:
            continue
        if lat > 90 or lat < -90 or lon > 180 or lon < -180:
            continue

        #date = row[head.index('created_at')].split()[0]
        date = int(time.mktime(time.strptime(row[head.index('created_at')],"%Y-%m-%d %H:%M:%S")))

        newrow = [row[head.index('atlas_id')],str(date),row[head.index('provider')]]
        newrow.extend([str(lat),str(lon),str(width),str(height)])
        print ','.join(newrow)