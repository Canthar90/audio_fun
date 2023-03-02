import wave
import time
import sys

import pyaudio


CHUNK = 960
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
p = pyaudio.PyAudio()



with wave.open("Gdzie-Ta-Keja.wav", "rb") as wf:
    
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        # If len(data) is less than requested frame_count, PyAudio automatically
        # assumes the stream is finished, and the stream stops.
        return (data, pyaudio.paContinue)
    
    
    
stream = p.open(format=pyaudio.paFloat32, channels=CHANNELS, rate=RATE, input=True, input_device_index=1, frames_per_buffer=CHUNK, stream_callback=callback)
while stream.is_active():
        time.sleep(0.1)
        
stream.close()
p.terminate()