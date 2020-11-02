import csv
import re
from datetime import datetime

lines = []
# open file as read-only
with open('CRS_POST_Output.csv', "r", newline='') as data:
    reader = csv.reader(data)
    # go over all of its rows, and the row's items and change 
    # items that match the date format
    for row in reader:
        for i, string in enumerate(row):
            if re.match(r"\d+\/\d+\/\d+", string):
                datetimeobject = datetime.strptime(string, '%m/%d/%Y')
                new_string = datetimeobject.strftime('%a, %d %b %Y %H:%M:%S %z')
                row[i] = new_string
                # print("Replaced", string, "with", new_string)
        # save edited, and originally correct ones to new list
        new_row = row
        lines.append(new_row)

# write new rows by overwriting original file
with open('CRS_POST_Output.csv', "w", newline='') as data:
    writer = csv.writer(data)
    writer.writerows(lines)