import pandas as pd
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import datetime

# Function to prettify the XML
def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Load the CSV file into a dataframe
df = pd.read_csv('SearchResults.csv')

# Create the root rss element
rss = Element('rss')
rss.set('version', '2.0')

# Create the channel element
channel = SubElement(rss, 'channel')

# Add title, link, and description to channel
title = SubElement(channel, 'title')
title.text = "Congressional Research Service Reports"

link = SubElement(channel, 'link')
link.text = "https://crsreports.congress.gov/"

description = SubElement(channel, 'description')
description.text = "RSS Feed for reports published by the Congressional Research Service."

# Loop through each row of the dataframe
for _, row in df.iterrows():
    # Create an item element for each row
    item = SubElement(channel, 'item')
    
    # Add title, link, pubDate, guid, and description to item
    title = SubElement(item, 'title')
    title.text = row['Title']
    
    link = SubElement(item, 'link')
    # Remove 'download' and the last segment from the URL
    url_parts = row['Url'].split('/')
    corrected_url = '/'.join(url_parts[:-2]).replace('/download', '')
    link.text = corrected_url  # Use the corrected URL here
    
    pubDate = SubElement(item, 'pubDate')
    # Format the date in the RFC 822 format which is used by RSS
    cover_date = datetime.datetime.strptime(row['CoverDate'], '%m/%d/%Y')
    pubDate.text = cover_date.strftime('%a, %d %b %Y %H:%M:%S +0000')
    
    guid = SubElement(item, 'guid')
    guid.set('isPermaLink', 'false')
    guid.text = row['ProductNumber']
    
    description = SubElement(item, 'description')
    description.text = row['Title']

# Convert the rss element and its children to a pretty-printed XML string
rss_xml = prettify(rss)

# Write the XML string to a file
with open('rss_feed.xml', 'w') as f:
    f.write(rss_xml)