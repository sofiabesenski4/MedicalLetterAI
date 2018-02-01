#Categorize_MTSample_Paragraphs.py

import os
import sys
import re



fp = open("example.txt","r")
S_fp = open("example_S.txt", "w")
B_fp = open("example_B.txt", "w")
A_fp = open("example_A.txt", "w")
R_fp = open("example_R.txt", "w")

data = fp.read()
print(data)
#This regular expression will capture the header to each paragraph, 
#	as well as the succeeding paragraph as group 0 and 1

paragraph_pattern = re.compile(r'b>(.*?)</b>(.*?)<', re.S)



for group in re.findall(paragraph_pattern, data):
	print("header:",group[0].strip().replace(":","").replace("  "," "))
	print("text:",group[1].strip().replace(":","").replace("  "," "))


