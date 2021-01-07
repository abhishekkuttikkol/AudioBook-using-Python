import pyttsx3
import PyPDF2


def audio_playback(text):
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[0].id)
    speaker.setProperty('rate', 100)
    speaker.say(text)
    speaker.runAndWait()


book = open('#Name of your pdf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('Total',pages,'pages')
for i in range(2,pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    
    audio_playback(text)
    

    
	

