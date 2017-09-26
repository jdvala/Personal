#! /usr/bin/env python
# encoding: utf-8

# Script to exract text from pdf files as well as scanned documents

#importing the dependencies

import PyPDF2
import textract
import os 


#defining the path

path = '' #enter the path where to find the files

for subdir, dirs, files in os.walk(path): # iterating over the files and sub folders
    for file in files:
        if file.endwith((".pdf")):
            a = os.path.join(subdir, file)
            
            pdfObject = open(a,'rb') # created  pdf object to open and access the files

            read_file = PyPDF2.PdfFileReader(pdfObject) # Read the file
            num_of_pages = read_file.numPages
            page_counter = 0
            text = ''
            # The while loop will itreate through all the pages and read each pag
            while page_counter < num_of_pages:
                pageObject = read_file.getPage(page_counter)
                page_counter = page_counter + 1
                text = text + pageObject.extractText()
#Now we have to check if the file is scanned or if the text is readable or not
                if text != "":
                    text = text
                else:
                    text = textract.process(a, method = 'tesseract', language = 'eng')





          
