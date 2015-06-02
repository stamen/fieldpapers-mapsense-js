#! /usr/bin/env python

import csv

head = None
doc = csv.reader(open('boxes.csv'), dialect='excel', delimiter='\t')
for row in doc:
    if not head:
        head = row
        newrow = row
        newrow.extend(['lat','lon','width','height'])
        print ','.join(newrow)
    else:
        west = float(row[head.index('west')])
        south = float(row[head.index('south')])
        east = float(row[head.index('east')])
        north = float(row[head.index('north')])
        lat = (north + south) / 2
        height = north - south
        lon = (east + west) / 2
        width = east - west

        if north > 90 or north < -90 or west > 180 or west < -180:
            continue
        if south > 90 or south < -90 or east > 180 or east < -180:
            continue
        if lat > 90 or lat < -90 or lon > 180 or lon < -180:
            continue

        newrow = row
        newrow.extend([str(lat),str(lon),str(width),str(height)])
        print ','.join(newrow)