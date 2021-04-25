from PIL import Image
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
import pytesseract
im=Image.open("testoc.jpg")
mytext=pytesseract.image_to_string(im,lang='eng')
print(mytext)
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
#print("donee")  
# Playing the converted file 
