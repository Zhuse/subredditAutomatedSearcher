import pyttsx3;

VOICE_INDEX = 1 #Indexes being at 0
SPEECH_WORDS_PER_MINUTE = 140
SPEECH_VOLUME = 0.3

def talk(word):
	
	engine = pyttsx3.init();
	allVoices = engine.getProperty('voices')

	engine.setProperty('voice', allVoices[VOICE_INDEX].id)
	engine.setProperty('rate', SPEECH_WORDS_PER_MINUTE)
	engine.setProperty('volume', SPEECH_VOLUME)

	engine.say("There is a post on r/mechmarket that matches key word " + word)
	engine.runAndWait() 

talk('MECHMARKET')