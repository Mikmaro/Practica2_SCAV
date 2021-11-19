# Mario Fernández
# Exercise 2

"""
En la codumentación encontré la comanda con ffplay, pero reemplazando esto por
ffmpeg -i input_video.mp4
de esta manera, permitirá utlizar este vídeo como input y resultará como ouptut
el vídeo histogram.mp4
"""

import os
import wget


def yuv_histogram():
    url1 = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url1)
    # El vídeo descargado es cut_video_12_seconds.mp4, es el mismo que se
    # ha creado en el ejercicio anterior

    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" ' \
          'histogram.mp4 '

    os.system(cmd)


if __name__ == '__main__':
    yuv_histogram()
