import librosa
import numpy as np
import librosa.display
import wave
import scipy
from scipy import stats
import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display
import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import scipy.io.wavfile as wav
from scipy import signal

def get_library():
    library = []
    name_file = open("names.txt")
    for line in name_file:
        line = line.strip()
        y, sr = librosa.load("sound_libary/" + line, sr=44100)
        library.append([y, sr, line])
    return library


def get_winner(sound, lib):
    cor_max = 0
    cor_i = 0
    for i in range(len(lib)):
        sample = lib[i][0]
        print("calculating start")
        cor = signal.fftconvolve(sample, sound[::-1], mode='valid')
        print("calculating done")

        if max(cor) > cor_max:
            cor_max = max(cor)
            cor_i = i
    return cor_i, lib[cor_i]


def record_audio(output_filename):
    fs = 44100
    duration = 10  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')
    print("Starting of writing audio")
    sd.wait()
    sd.play(myrecording, fs)

    print("Writing is end")
    write(output_filename, fs, myrecording)


def find_most_similar(filename):
    y, sr = librosa.load(filename, sr=44100)  # в идеале с микро взять
    # x = y
    # X = librosa.stft(x)
    # Xdb = librosa.amplitude_to_db(abs(X))
    # plt.figure(figsize=(14, 5))
    # librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    # plt.colorbar()

    # plt.figure(figsize=(14, 5))
    # librosa.display.waveplot(y, sr=sr)
    # plt.show()

    lib = get_library()  # y- то шо нам нужно чистая как какаин вейформа sr частота дискретизации

    num_in_library, guessed_track = get_winner(y, lib)
    return guessed_track[2]

if __name__ == '__main__':
    name = "sound_to_find/bibi.wav"
    record_audio(name)
    res_name = find_most_similar(name)
    os.startfile(r"sound_libary\\" + res_name)
