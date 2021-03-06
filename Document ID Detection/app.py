# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:44:03 2020

@author: basil_chacko_mathew
Prgt Breaf: Identify The number from a PDF Document by the help of OCR. Dectect through NLP Search Method.
"""
#import header
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import glob, re, os

#specify the path in this text file.
line=open('C:\PDFRENAME\\textfile.txt').read()

#read all PDF files from that dir
pdfs = glob.glob(r""+line+"*.pdf")
for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500)
    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')
        #Here we Check the 2nd page only....
        if pageNum ==1:
            pattern = 'Document Number: (\d{6}.\d*)'
            outtext =re.findall(pattern, text)
            newfile = os.path.join(line, outtext[0]+'.pdf')
            os.rename(pdf_path, newfile)
            print(outtext[0])
    
            