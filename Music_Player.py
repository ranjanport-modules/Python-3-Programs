from pygame import mixer

name = input("Search: ")
filename = name
files= filename.join(".mp3")
file = files
mixer.init()
mixer.music.load(file)
mixer.music.play()