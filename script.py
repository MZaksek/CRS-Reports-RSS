# Import the necessary libraries
import pandas as pd  # Used for handling the CSV file and data manipulation
from xml.etree.ElementTree import Element, SubElement, tostring  # Used for creating and handling XML elements
from xml.dom import minidom  # Used for prettifying the XML
import datetime  # Used for handling dates and times

# Define some constants
CSV_FILE = 'SearchResults.csv'  # The name of the CSV file to read from
OUTPUT_FILE = 'rss_feed.xml'  # The name of the XML file to write to
RSS_VERSION = '2.0'  # The RSS version to use
FEED_TITLE = "Congressional Research Service Reports"  # The title of the RSS feed
FEED_LINK = "https://crsreports.congress.gov/"  # The link associated with the RSS feed
FEED_DESCRIPTION = "RSS Feed for reports published by the Congressional Research Service."  # A description of the RSS feed
NUM_REPORTS = 500  # The number of reports to include in the RSS feed

# Function to prettify the XML
def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    # Convert the element to a string
    rough_string = tostring(elem, 'utf-8')
    # Parse the string into an XML document and return a pretty-printed version of it
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Function to create an RSS item
def create_item(row):
    """
    Create an RSS item based on a row of the DataFrame and add it to the channel.
    """
    # Create an item element and add it to the channel
    item = SubElement(channel, 'item')
    
    # Add the title of the report to the item
    title = SubElement(item, 'title')
    title.text = row['Title']
    
    # Add the URL of the report to the item, after removing 'download' and the last segment from the URL
    link = SubElement(item, 'link')
    url_parts = row['Url'].split('/')
    corrected_url = '/'.join(url_parts[:-2]).replace('/download', '')
    link.text = corrected_url  # Use the corrected URL here
    
    # Add the publication date of the report to the item, in the RFC 822 format used by RSS
    pubDate = SubElement(item, 'pubDate')
    cover_date = datetime.datetime.strptime(row['CoverDate'], '%m/%d/%Y')
    pubDate.text = cover_date.strftime('%a, %d %b %Y %H:%M:%S +0000')
    
    # Add the product number of the report to the item, as a guid (globally unique identifier)
    guid = SubElement(item, 'guid')
    guid.set('isPermaLink', 'false')  # The guid is not a permalink
    guid.text = row['ProductNumber']
    
    # Add the title of the report to the item, as a description
    description = SubElement(item, 'description')
    description.text = row['Title']

# Load the CSV file into a dataframe
df = pd.read_csv(CSV_FILE)

# Create the root rss element and set its version
rss = Element('rss')
rss.set('version', RSS_VERSION)

# Create the channel element and add it to the rss element
channel = SubElement(rss, 'channel')

# Add the title, link, and description to the channel
title = SubElement(channel, 'title')
title.text = FEED_TITLE

link = SubElement(channel, 'link')
link.text = FEED_LINK

description = SubElement(channel, 'description')
description.text = FEED_DESCRIPTION

# Loop through the first NUM_REPORTS rows of the dataframe
for _, row in df.head(NUM_REPORTS).iterrows():
    # For each row, create an RSS item
    create_item(row)

# Convert the rss element and its children to a pretty-printed XML string
rss_xml = prettify(rss)

# Write the XML string to a file
with open(OUTPUT_FILE, 'w') as f:
    f.write(rss_xml)
