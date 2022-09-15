from email.mime import audio
from tracemalloc import start
import pyaudio
import wave

Frames_Per_Buffer = 3200
Format = pyaudio.paInt16
Channels = 1
Rate = 16000

P = pyaudio.PyAudio()

Recorder = P.open(
    format = Format,
    channels = Channels,
    rate = Rate,
    input = True,
    frames_per_buffer = Frames_Per_Buffer
)

print('Start Recording')

seconds = 5
track_name = 'Track.wav'
frames = []

def audio():
    for i in range(0,int(Rate/Frames_Per_Buffer*seconds)):
        Recording = Recorder.read(Frames_Per_Buffer)
        frames.append(Recording)

    Recorder.stop_stream()
    Recorder.close()
    P.terminate



    audio_track = wave.open(track_name,"wb")
    audio_track.setnchannels(Channels)
    audio_track.setframerate(Rate)
    audio_track.setsampwidth(P.get_sample_size(Format))
    audio_track.writeframes(b"".join(frames))
    audio_track.close()
    print('recorded')
    return audio_track
