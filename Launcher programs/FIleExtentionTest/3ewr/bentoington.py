import random
import pyttsx3
import time

word_list = ["ben", "troen", "benjamin", "bennington", "noteblockington", "noteblockistan", "troenton", "tronnington", "tronningson", "ten", "tennington", "tenningson", "the I", "the II", "the III", "the IIII", "royal member of the noteblockistan family", "royal member of the benningson family", "benningson", "block", "blockington", "blockingson", "t. block", "t. notington", "t. blockington", "t. noteblockson", "t. noteblockington", "b.", "noteblock", "blockingson", "tennison", "blockinton", "nbsington", "(used to be called not-a-block in middle school)", "(his great-great-grandfather used to own a note-block studio)", "trowlington", "trowel", "troent-trowling", "trainingson", "trainington", "bentenningsen"]
def generate_sentence():
    sentence_length = random.randint(2, 10)
    sentence = []
    last_word = None
    for i in range(sentence_length):
        word = random.choice(word_list)
        if i == sentence_length - 2 and 'royal' in sentence:
            index = sentence.index('royal')
            if index > 0:
                sentence[index-1:index+1] = [' '.join(sentence[index-1:index+1])]
            else:
                sentence[index:index+2] = [' '.join(sentence[index:index+2])]
        sentence.append(word)
    return ' '.join(sentence)

def text_to_speech(text, wpm):
    engine = pyttsx3.init()
    engine.setProperty('rate', wpm)
    engine.say(text)
    engine.runAndWait()

sentence = generate_sentence()
print(sentence)
text_to_speech(sentence, 120/1)  # Speed of 10 words per minute
