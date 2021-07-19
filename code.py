"""
Created on Mon Jul 19 22:08:17 2021

@author: raja sekhar
"""

import pytesseract
import cv2

#Modify the address to SMS screenshot jpeg file address
orig=r"C:\Users\...\test.jpeg"

# Reading image
img=cv2.imread(orig)

# Sending image to tesseract engine
output = pytesseract.image_to_string(img)

# Splitting ocr output into words
strings=output.split()

# Printing words containing "http"
for word in strings:
    if "http" in word:
        print(word)
