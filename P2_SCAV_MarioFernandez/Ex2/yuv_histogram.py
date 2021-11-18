# Mario Fernández
# Exercise 2

"""
Antes que nada, para poder utilizar el script de Python llamandolo desde la terminal de
Ubuntu debí importar os, lo que permite escribir comandas en Python para poder pasarlas
a Ubuntu y que se puedan ejecutar desde la terminal. Esto también lo importaré para los
siguientes ejercicios
"""

import os


def yuv_histogram():
    cmd = 'ffplay cut_video_12_seconds.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"'
    os.system(cmd)


if __name__ == '__main__':
    yuv_histogram()
