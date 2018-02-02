#Letter_To_Text.py
#Date Feb 1 2018
#most code is adapted from the example at https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

"""
Feb 2nd 2018:
Notes:
-100dpi image returned TERRIBLE results
-300 DPI image returned PERFECT text translation

-not able to interpret pdf files, for some reason. 
	There are sources online stating that there is a module i need to install to be able
	to achieve this, but quite frankly, working with all these new libraries is EXCRUTIATING
	and it seems smarter to convert the pdfs to jpgs because I think they are compressed
- able to interpret jpg, jpeg, png files
"""

import pytesseract
import argparse
import cv2
import os
from PIL import *
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help = "path to input image to be OCRd")
ap.add_argument("-p","--preprocess",type = str,default = "thresh")
args = ap.parse_args()

#loading image and convert to grayscale
image = cv2.imread("test1.bmp")
print(image.shape)
cv2.imshow("img,",image)
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

"""HERE IS WHERE WE CAN ADD IN OUR OWN FILTERS/PREPROCESSING EFFECTS TO INCREASE OCR ACCURACY DEPENDING ON DATA
"""
#check to see if we are applying a thresholding to preprocess the image
if args.preprocess == "thresh" :
	#gray = cv2.threshold(gray, 0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	gray = cv2.threshold(gray, 0, 256, cv2.THRESH_OTSU)[1]

#make a check to see if median blurring should be done to remove noise
elif args.preprocess=="blur":
	gray = cv2.medianBlur(gray,3)
	
#write the image file temporarily to disk so we can OCR it with the pytesseract interface, accessing
# the (natively Java) tesseract application 

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename,gray)


#we can finally apply tesseract to the saved image using python bindings, while removing the temp image from disk
text = pytesseract.image_to_string(Image.open(filename))
#os.remove(filename)
print(text)

cv.imshow("Image",image)
cv.imshow("Output", gray)
cv2.waitKey(0)

