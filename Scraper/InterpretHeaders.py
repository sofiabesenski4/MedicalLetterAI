#InterpretHeaders.py
#Author: Thomas Besenski
#Date created: Jan 30th 2018
"""
The purpose of this script is to fulfill step #1 from the sample generation workflow described in the ppt presentation

"""

import os
import sys
import re

#writing a regex to capture all the text stored in <b>...</b> tags in the txt document

pattern = r'<b>(.*?)</b>'


#from stack overflow : https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
#getting the names of all the files stored within that folder
file_list = []
for file in os.listdir("Scraped-Article-Content-MedicalTranscriptionSamples"):
    if file.endswith(".txt"):
        file_list.append(os.path.join("Scraped-Article-Content-MedicalTranscriptionSamples", file))	

"""
Now we are creating a dictionary which will hold key:value pairs ("Header": # of occurences in all files)
"""
headers = {}
for file_name in file_list:	
	fp = open(file_name, "r")
	data = fp.read()
	file_headers = re.findall(pattern, data)
	for header in file_headers:
		if header not in headers:
			headers[header] = 1
		else:
			headers[header]+=1
pairs = []
for item in headers.items():
	pairs.append(item)
pairs.sort(reverse = True, key = lambda x: x[1])
print (pairs)
#at this point, a dictionary is printed, in descending order of header appearance

