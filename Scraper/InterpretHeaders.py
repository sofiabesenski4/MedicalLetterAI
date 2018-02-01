#InterpretHeaders.py
#Author: Thomas Besenski
#Date created: Jan 30th 2018
"""
The purpose of this script is to fulfill step #1 from the sample generation workflow described in the ppt presentation

"""

import os
import sys
import re



"""
This function will take a list of tuples, (Header title, number of paragraphs),
and will take a corresponding category mapping stored in category_dict {Pattern: Resulting categorization }
"""
def categorize_headers(headers_list, categorization_dict):
	for item in headers_list:
		for key in categorization_dict:
			if re.search(key.upper(),item[0]) != None:
				category_dict[category_dict[key].upper()]+=item[1]
				pairs.remove(item)
				categorized_paragraphs+=item[1]
				break
	return
#writing a regex to capture all the text stored in <b>...</b> tags in the txt document

pattern = r'<b>(.*?)</b>'


#from stack overflow : https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
#getting the names of all the files stored within that folder
file_list = []
for file in os.listdir("Scraped-Article-Content-MedicalTranscriptionSamples"):
    if file.endswith(".txt"):
        file_list.append(os.path.join("Altered-MTSamples", file))	

"""
Now we are creating a dictionary which will hold key:value pairs ("Header": # of occurences in all files)
"""
total_paragraphs_processed = 0
headers = {}
for file_name in file_list:	
	fp = open(file_name, "r")
	data = fp.read()
	file_headers = re.findall(pattern, data)
	for header in file_headers:
		if re.sub("  ", " ",re.sub("MEDICAL","",header).strip().strip(":").upper()) not in headers:
			headers[re.sub("  ", " ",re.sub("MEDICAL","",header).strip().strip(":").upper())] = 1
			total_paragraphs_processed+=1
		else:
			headers[re.sub("  ", " ",re.sub("MEDICAL","",header).strip().strip(":").upper())]+=	1
			total_paragraphs_processed+=1
pairs = []
for item in headers.items():
	pairs.append(item)
pairs.sort(reverse = True, key = lambda x: x[1])
print ([x for x in pairs if x[1]>9])
#at this point, a dictionary is printed, in descending order of header appearance, and for entries who's frequency is greater than 9
# to eliminate the large amount of unique tags

#now I am trying to compile dividing header strings which would separate the paragraphs into the categories
"""
IDEA:
Hold a dictionary, who's keys are keywords contained in headers recognized in this script, 
and who's element corresponds to the categorizing set "S","B","A","R"
"""
category_dict = {"DISCHARGE":"R", "HISTOR":"B", "PROCEDURE":"A","COMPLAINT":"S", "DIAGNO":"R",
				"SITUATION":"S","BACKGROUND":"B"}
category_count_dict = {"S":0, "B":0, "A":0,"R":0}
categorized_paragraphs = 0
for item in pairs:
	for key in category_dict:
		if re.search(key.upper(),item[0]) != None:
			category_count_dict[category_dict[key].upper()]+=item[1]
			pairs.remove(item)
			categorized_paragraphs+=item[1]
			break
print (category_count_dict.items())
print("total paragraphs processed", total_paragraphs_processed)
print("total paragraphs categorized", categorized_paragraphs)

