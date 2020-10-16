# pip install pyttsx3
import pyttsx3
import PyPDF2

book = open('demo.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
# find all pages
for num in range(0, pages):
    pages = pdfReader.getPage(0)
    text = pages.extractText()
    speaker.say(text)
    speaker.runAndWait()
