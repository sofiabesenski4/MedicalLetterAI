#Scrape-MTSamples.py is a script which will iterate through all ~300 something pages of 
#MedicalTranscriptions.com to get all the sample medical transcripts stored in its blog posts
# and save them into individual text files in a folder where this script is located on disk

#This script is website specific, and cannot be applied directly to other websites, although. the concepts here
#can be applied to other web scrapers.
#

"""
Author: Thomas Besenski
Date: Jan 23 2018


"""
from queue import *
import datetime
import random
import urllib.request
import re
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import sys

"""
PSEUDOCODE:

-Get URL response from http://www.Medicaltranscriptionsamples.com

-while the URL response delivers a url that we requested (we didnt hit the end of the list of pages) 

	-Use the httpresponse to build a BS object
	-Go into the content class contained within the html file
	-For every link in the content div that we have not encountered, add it to a list of article urls
	
-for every url in the list of urls:
	-follow the link
	-get the title of the article (h1 tag)
	-get the contents of the article (post-content tag)

	-save the text contained in the article into a text file

"""

"""
getResponse function will return an HTTPResponse object from the parameter url
"""
def getResponse(url):
    try: 
        #print ("url =  " +url)
        response = urllib.request.urlopen(url)
        #DEBUG
        #print ("This is the url of the html file we requested: " + url)
        #print ("this is the url of the response reached: " + response.geturl())
        return response
    except HTTPError as e:
        print (e)
        return None


"""
Function: append_sample_links(HTTPResponse object, list or urls)
output: will return a reference to the sample_url list containing an updated list of urls to article pages

Note: you do not need to explicitly return a reference to the sample_url since the parameter is pass by reference
but I did it anyway to increase readability.
"""
def append_sample_links(response, sample_urls):
	#make a BS object to parse the html page
	soup = BeautifulSoup(response, "html.parser")
	
	#find all the divs which contain the class "type-post"
	for element in soup.body.find_all(class_="type-post"):	
		#for every link contained within the type-post div
		for link in element.find_all("a"):
			#if the link is an external reference
			if "href" in link.attrs:
				#if the link has not already been recorded, add it to the list or urls
				if link.attrs['href'] not in sample_urls:
					sample_urls.append(link.attrs["href"])
	return sample_urls
	
"""
function: get_article_text(article number/number of article encountered, url of new article to be processed)
output:none
side-effects: will create a text file storing the content of an article, named the integer specified first-input-parameter.txt
"""	
def get_article_text(article_num, url):
	#create new text file for this article
	fp = open("Scraped-Article-Content-MedicalTranscriptionsamples.com/" + str(article_num) + ".txt", "w")
	# open the folder called Scraped-Article-Content-MedicalTranscriptionsamples.com in the pwd
	response = getResponse(url)
	soup = BeautifulSoup(response, "html.parser")
	sample_title = soup.h1.contents
	
	contents_of_sample = (list(soup.find_all(class_="post-content")))[0]
	#print(sample_title[0], ":",contents_of_sample.find_all("p"))
	fp.write(sample_title[0] + "\n")
	for paragraph in contents_of_sample.find_all("p"):
		#print (str(paragraph),"\n")
		fp.write(str(paragraph).replace("</br>", "").replace("<br>", "\n") + "\n")
	
	#regex: re.findall(r'<p>(.*)</p>', 
def main():
	"""
	This part of the function gets all the sample_urls
	"""
	url_format = "http://www.medicaltranscriptionsamples.com/page/"
	i=1
	sample_urls = []
	#iterating through every page listed in http://www.MedicalTranscriptionsamples.com/page/<page #>
	while True:
		url = url_format + str(i)
		response = getResponse(url)
		#if the response we get from trying to access another page of the website returns a page not found, then
		#we know that there is no more pages to be scraped
		if response.geturl() == "http://www.medicaltranscriptionsamples.com/my404/":
			break 
		append_sample_links(response,sample_urls)
		i+=1
		
	#for every sample url in the list, process it and save certain contents to an external file
	for x, sample_url in enumerate(sample_urls):
		get_article_text(x, sample_url)
		
	
main()
