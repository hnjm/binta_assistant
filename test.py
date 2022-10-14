

def clear_blank_space(string):
    string =  string.split(' ')
    new_string = [el for el in string if el !='']
    return " ".join(new_string)

def clear_speech(original_speech, badwords):
    new_speech = original_speech
    for word in badwords:
        new_speech= new_speech.replace(word, "")
    return clear_blank_space(new_speech)






stre = clear_speech('merci je te vois venir', ['je', 'te']) #merci voir venir

print(stre )