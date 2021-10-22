from vlc import Instance
import time
import os
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib

class VLC:
    def __init__(self):
        self.Player = Instance('--loop')

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        path = "C:\\Users\\Gaurav7.G7\\Desktop\\SONGS-MP3"
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()


# Create a object
player = VLC()
# Add playlist
player.addPlaylist()

while True:
    a= int(input("play songs:"))
    #Play the song
    if a==1:
        player.play()
        time.sleep(1)

    # Play the next song
    
    elif a==2:
        player.next()
        time.sleep(1)

    # Pause the song
    elif a==3:
        player.pause()
        time.sleep(1)

    # Resume the song
    elif a==4:
        player.play()
        time.sleep(1)

    # Previous song
    elif a==5: 
        player.previous()
        time.sleep(1)
    
    # Stop the song
    elif a==6:
        player.stop()

    elif 'on youtube' in query:
            query = query.replace("on youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            speak(f" showing {query} on youtube.")
