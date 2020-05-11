import librosa
import numpy as np
import librosa.display
import scipy
from scipy import stats
import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display



def get_library():
    library = []
    name_file = open("names.txt")
    for line in name_file:
        line = line.strip()
        y, sr = librosa.load("sound_libary/" + line, sr=None)  # todo delete /n at the end of raw
        library.append([y, sr, line])
    return library


def get_winner(sound, lib):
    cor_max = 0
    cor_i = 0
    for i in range(len(lib)):
        sample = lib[i][0]
        print("calculating start")
        cor = np.correlate(sample, sound)
        print("calculating done")

        if max(cor) > cor_max:
            cor_max = max(cor)
            cor_i = i
    return cor_i, lib[cor_i]


if __name__ == '__main__':
    ipd.Audio("sound_libary/system.wav")
    y, sr = librosa.load("sound_libary/system.wav", sr=None)# в идеале с микро взять

    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y, sr=sr)
    plt.show()

    lib = get_library()  # y- то шо нам нужно чистая как какаин вейформа sr частота дискретизации

    num_in_libary, gused_track = get_winner(y, lib)

    # куча таких это библиотека будет
    # какая то входная последовательнасть можно с микро можно просто кусок

    # потом нумпаем а еще лучше нумпаем и нашими функциями находим кореляцию котора массив для каждого из либы
    # у кого в массиве максимум тот и вин
