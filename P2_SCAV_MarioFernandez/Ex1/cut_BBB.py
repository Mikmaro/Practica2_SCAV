# Mario Fernández
# Exercise 1

import os

"""
Antes que nada, para poder utilizar el script de Python llamandolo desde la terminal de
Ubuntu debí importar os, lo que permite escribir comandas en Python para poder pasarlas
a Ubuntu y que se puedan ejecutar desde la terminal. Esto también lo importaré para los
siguientes ejercicios

El vídeo input sería Big_Buck_Bunny.mp4, la variable cut_time serían los segundos en los
que se desee cortar (input del usuario), y el video de salida sería cut_video_12_seconds.mp4
"""


def cut_BBB(cut_time):
    cmd = 'ffmpeg -ss 0 -i Big_Buck_Bunny.mp4 -c copy -t ' + cut_time + ' cut_video_12_seconds.mp4'
    os.system(cmd)


if __name__ == '__main__':
    cut_video_frame = str(input("Seleccione el tiempo (segundos) de corte: "))
    cut_BBB(cut_video_frame)
