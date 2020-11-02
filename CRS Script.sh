#!/bin/sh
# This program retrieves recent Congressional Research Service reports
# from the crsreports.congress.gov website, stores them in a csv
# and constructs an rss feed, to be used in feed readers

# Send a POST request to the CRS website.
# Request returns listing of all CRS reports,
# which the script writes to a csv file
curl -d "orderBy=Date&pageNumber=0" https://crsreports.congress.gov/Search/GetCsvForFixedNumberSearchResults/ ls > CRS_POST_Output.csv

# Report links, when visited, by default prompt the user to
# download the PDF file. This below command removes the download
# function, so the reports are viewable in the browser
sed -i '' -e 's,/download/,/,g' CRS_POST_Output.csv

# These search and replace functions fixe potentially problematic characters
sed -i '' -e 's,&,(ampersand),g' CRS_POST_Output.csv

# To work correctly in rss feeds, the dates need to be formatted in a certain way.
# Dates are, by default, sorted in the following way: MM/DD/YYYY.
# However we need to format them according to the RFC 822 Date and Time Specification.
python3 Modify_CSV.py

# Now, we will take the data from the csv file and print it
# into an xml file, formatted as an rss feed
python3 print_xml.py

echo Script has run successfully!
