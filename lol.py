import librosa
import numpy as np
import librosa.display
import scipy
from scipy import stats


def get_library():
    library = []
    name_file = open("names.txt")
    for line in name_file:
        y, sr = librosa.load("sound_libary/" + line, sr=None)
        library.append(y)
    return library


if __name__ == '__main__':
    lib = get_library()  # y то шо нам нужно чистая как какаин вейформа sr частота дискретизации
    
    # куча таких это библиотека будет
    # какая то входная последовательнасть можно с микро можно просто кусок

    # потом нумпаем а еще лучше нумпаем и нашими функциями находим кореляцию котора массив для каждого из либы
    # у кого в массиве максимум тот и вин
