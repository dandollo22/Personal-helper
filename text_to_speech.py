 from gtts import gTTS 
import os 
  
text = 'Welcome !'
language = 'en'

# Convert  
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Save 
myobj.save("file.mp3") 
  
# Play 
os.system("file.mp3") 