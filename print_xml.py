# This script writes data from the csv into an xml to be used by feed readers

import csv

with open('CRS_POST_Output.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    array_length = len(data)
    

rss_feed = open('rss_feed.xml', 'w') 

print('<?xml version="1.0" encoding="UTF-8" ?>', file = rss_feed)
print('<rss version="2.0">\n', file = rss_feed)

print('<channel>', file = rss_feed)
print('\t<title>Congressional Research Service Reports</title>', file = rss_feed)
print('\t<link>https://crsreports.congress.gov/</link>', file = rss_feed)
print('\t<description>This feed contains a listing of reports published by the Congressional Research Service. This is an UNOFFICIAL feed, generated using scripts created by Matthew Zaksek.</description>', file = rss_feed)

for i in range(1, array_length):
	print('\t<item>', file = rss_feed)
	print('\t\t<title>' + data[i][3] + '</title>', file = rss_feed)
	print('\t\t<description>' + data[i][3] + '</description>', file = rss_feed)
	print('\t\t<pubDate>' + data[i][2] + '-0600' + '</pubDate>', file = rss_feed)
	print('\t\t<link>' + data[i][4] + '</link>', file = rss_feed)
	print('\t</item>', file = rss_feed)

print('</channel>', file = rss_feed)
print('</rss>', file = rss_feed)
rss_feed.close()