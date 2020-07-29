import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    
	# read the audio data from the default microphone
	print("Listening...")
	audio_data = r.listen(source)
	
    # convert speech to text
	print("Converting...")
	try : 
		text = r.recognize_google(audio_data, language="en-EN")
	except : 
		text = "Speech not recognized !"

	print(text)

