#Categorize_MTSample_Paragraphs.py
#Author: Thomas Besenski
#Created: Jan 31, 2018
"""
IDEA:
Given a dictionary, mapping a header keyword to a resulting SBAR category, take that header and the following 
	paragraph of text, and store them (separated by a \n) in the corresponding text file
	
	Iterate through all the files, and filter the header/paragraph groups into the different categories using different
	dictionaries, which start off with good indication of  a proper categorization, and the last one would be a categorization
	rule which was made if nothing else was able to categorize the header/paragraph pair
	
	ie: for every dictionary/filter mapping we have came up with
	
	first dictionary/filtering iteration :
		{"History": Background File, "Situation": Situation File, 
		"Analysis": Analysis File, "Plan": Recommendation File}
		by applying each one of these regex keys to the file, we would filter out any header/paragraph pairs which would contain
		the most obvious indication of their proper respective categories
	
	second dictionary/filtering iteration:
		{ "Operation" : Analysis File, "Previous": Background File, "Complaint": Situation File, "Discharge": Recomendation File}
		the 
"""
import os
import sys
import re

#function takes the parameters:
#	categorical_dict = dictionary which maps a keyword/filter with a file pointer, pointing to the file that should be written to
#	data = string read from single file
def store_data_from_string(categorical_dict, data): 
	for group in re.findall(paragraph_pattern, data):
		print("header:",group[0].strip().replace(":","").replace("  "," "))
		print("text:",group[1].strip().replace(":","").replace("  "," "))
		for key in categorical_dict:
			if re.search(key,group[0])!=None:
				categorical_dict[key].write("header:"+group[0].strip().replace(":","").replace("  "," ")+"\n")
				categorical_dict[key].write("text:"+group[1].strip().replace(":","").replace("  "," ")+"\n")


fp1 = open("example.txt","r")
fp2 = open("example2.txt","r")
fp3 = open("example3.txt","r")
file_pointers = [fp1,fp2,fp3]
S_fp = open("example_S.txt", "w")
B_fp = open("example_B.txt", "w")
A_fp = open("example_A.txt", "w")
R_fp = open("example_R.txt", "w")


filter_1 = {"PREOPERATIVE":S_fp, "POSTOPERATIVE":R_fp, "PROCEDURE" : A_fp, "BACKGROUND" : B_fp}
filter_2 = {"COMPLAINT":S_fp, "HISTORY": B_fp , "ANALYSIS": A_fp , "PLAN": R_fp}

filters = [filter_1,filter_2]
#This regular expression will capture the header to each paragraph, 
#	as well as the succeeding paragraph as group 0 and 1
paragraph_pattern = re.compile(r'b>(.*?)</b>(.*?)<', re.S)
for 
store_data_from_string(first_filters, file_contents)
