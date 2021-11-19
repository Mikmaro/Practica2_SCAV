# Mario Fernández
# Exercise 5

"""
Utilizando info de las páginas siguientes para coger un poco de inspiración

https://www.it-swarm-es.com/es/python/crear-un-menu-en-python/1043095475/
https://www.lawebdelprogramador.com/codigo/Python/2935-Ejemplo-de-implementar-un-menu-en-python-en-la-consola.html

me fueron de mucha utilidad para refrescar aspectos necesarios para hacer el menú

El video de BBB original se llama Big_Buck_Bunny.mp4, y el cortado
se llama cut_video_12_seconds.mp4 (el cual se crea en el primer ejercicio)
"""

import os


# ex1
def cut_BBB(cut_time):
    cmd = 'ffmpeg -ss 0 -i Big_Buck_Bunny.mp4 -c copy -t ' + cut_time + ' cut_video_12_seconds.mp4'
    os.system(cmd)


# ex2
def yuv_histogram():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" ' \
          'histogram.mp4 '
    os.system(cmd)


# ex3
def resize_720p():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB720p.mp4'

    os.system(cmd)


def resize_480p():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB480p.mp4'

    os.system(cmd)


def resize_360_240():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -s 360x240 -c:a copy BBB360_240.mp4'

    os.system(cmd)


def resize_160_120():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -s 160x120 -c:a copy BBB160_120.mp4'
    os.system(cmd)


# ex4
def stereo_to_mono():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -ac 1 MONO_cut_video_12_seconds.mp4 '
    os.system(cmd)


def change_audio_codec():
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -vcodec copy -acodec mp3 mp3_cut_video_12_seconds.mp4'
    os.system(cmd)


# ex5
def menu():
    os.system('clear')

    print("Selecciona un ejercicio con las teclas [1][2][3][4], o [5] para salir:")

    print("\t[1] - Ejercicio 1: Recortarás el vídeo BBB a los primeros 12 segundos")

    print("\t[2] - Ejercicio 2: Mostrarás el histograma YUV junto al vídeo de 12 segundos. "
          "¡NECESITAS HABER HECHO PRIMERO EL EJERCICIO 1!")

    print("\t[3] - Ejercicio 3: Realizarás diferentes reescalados con el vídeo de 12 segundos. "
          "¡NECESITAS HABER HECHO PRIMERO EL EJERCICIO 1!")

    print(
        "\t[4] - Ejercicio 4: Crearás dos nuevos archivos, un archivo en formato MONO y otro con diferente codec de "
        "audio "
        "¡NECESITAS HABER HECHO PRIMERO EL EJERCICIO 1!")

    print("\t[5] - Salir ")


if __name__ == '__main__':
    while True:
        menu()
        ejercicio_escogido = input("Selecciona ejercicio: ")

        if ejercicio_escogido == "1":

            cut_video_frame = str(input("Seleccione el tiempo (segundos) de corte: "))
            cut_BBB(cut_video_frame)

        elif ejercicio_escogido == "2":

            yuv_histogram()

        elif ejercicio_escogido == "3":

            resize_720p()
            resize_480p()
            resize_360_240()
            resize_160_120()

        elif ejercicio_escogido == "4":

            stereo_to_mono()
            change_audio_codec()

        elif ejercicio_escogido == "5":
            break

        else:
            input("Ese ejercicio no existe. Escoge de nuevo: ")
