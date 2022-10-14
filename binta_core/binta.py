import pyttsx3
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

voice = engine.getProperty('voices')[0] # the french
print(voice)
#voice = engine.getProperty('voices')[1] # the english voice
engine.setProperty('voice', voice.id)


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


def intro():
    engine.say("Bonjour, aboubakar. est tu prêt pour me développer?")
    engine.say("tu dois savoir, je dois être super intélligent")
    engine.say("grâce à moi, on doit pouvoir manipuler odou pour gérer les activités commerciales d'une entreprise")
    engine.say("dis moi quelque chose je répètes tu entends ")
    engine.runAndWait()

def speak(text):
    
    engine.say(text)
    engine.runAndWait()