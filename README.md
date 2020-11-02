# CRS-Reports-RSS
These scripts will fetch the updated list of reports from the Congressional Research Service, and export them into an xml RSS feed.

# Instructions
If using Mac, first download "CRS Script.sh", "Modify_CSV.py" and "print_xml.py" and place all three files in a single folder.

Then, navigate to the folder and have it open in Finder.

Open a new Terminal window, type "cd", type a space, and drag your folder to the Terminal window and press the "enter/return" key.

Then, to start the script, drag the "CRS Script.sh" file to the Terminal window, and again press the "enter/return" key.

The program will now run, creating two new files. The first is the "CRS_POST_Output.csv", which contains the modified data returned by the CRS website in spreadsheet form.

The second is rss_feed.xml, which is the outputted RSS feed, which can be used in any feed reader software.

Each time the program is run, the feed will be updated based on the current listing from the CRS website.
