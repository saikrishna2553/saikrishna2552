from gtts import ga
import os
text="kk.txt"
audio="audio.mp3"
def text_to_audio(text,audio):
    file=open(text,'r',encoding='utf_8')
    read_data=file.read()
    ga=cd(text, lang='te')
    ga.save(audio)
    file.close()
text_to_audio(text,audio)
