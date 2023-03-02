import time
from pygame import mixer
from pygame import mixer, _sdl2 as devicer

mixer.pre_init(devicename='Mikrofon (KRUX EDIS 1000)') # Initialize it with the correct device
mixer.init()
mixer.music.load("Gdzie Ta Keja.mp3") # Load the mp3
mixer.music.play() # Play it

while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)