# Mario Fernández
# Exercise 2

"""
En la codumentación encontré la comanda con ffplay, pero reemplazando esto por
ffmpeg -i input_video.mp4
de esta manera, permitirá utlizar este vídeo como input y resultará como ouptut
el vídeo histogram.mp4
"""

import os


def yuv_histogram():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" ' \
          'histogram.mp4 '

    os.system(cmd)


if __name__ == '__main__':
    yuv_histogram()
