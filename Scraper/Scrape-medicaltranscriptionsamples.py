#Scrape-MTSamples.py is a script which will iterate through all ~300 something pages of 
#MedicalTranscriptions.com to get all the sample medical transcripts stored in its blog posts
# and save them into individual text files in a folder where this sript is located on disk
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
	-Go into the body of the BS object
	-For every link in the body that we have not encountered
		-go into the link
		-break it into a BSobject
		-go into the body
		-Find the part of the text that we want
		-save it to an external text file in  folder


"""

"""
getResponse function will return an HTTPResponse object from the parameter url
"""
def getResponse(url):
    try: 
        #print ("url =  " +url)
        response = urllib.request.urlopen(url)
        #DEBUG SHIT
        #print ("This is the url of the html file we requested: " + url)
        #print ("this is the url of the response reached: " + response.geturl())
        return response
    except HTTPError as e:
        print (e)
        return None



def append_sample_links(response, sample_urls):
	soup = BeautifulSoup(response, "html.parser")
	#url_pattern = re.compile(r'www.medicaltranscriptionsamples.com/(.*)/$')
	#contents_pattern = re.compile(r"Read more...")
	for element in soup.body.find_all(class_="type-post"):	
		for link in element.find_all("a"):
			#now we are looking at the links within posts
			if "href" in link.attrs:
				#print(link.attrs["href"])	
				if link.attrs['href'] not in sample_urls:
					sample_urls.append(link.attrs["href"])
	return sample_urls
	
	
def get_article_text(article_num, url):
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
		if response.geturl() == "http://www.medicaltranscriptionsamples.com/my404/":
			break 
		append_sample_links(response,sample_urls)
		i+=1
		
	#print (sample_urls)
	for x, sample_url in enumerate(sample_urls):
		get_article_text(x, sample_url)
		
	
main()
