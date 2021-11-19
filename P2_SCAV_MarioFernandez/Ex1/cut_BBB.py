# Mario Fernández
# Exercise 1

import os
import wget

"""
Antes que nada, para poder utilizar el script de Python llamandolo desde la terminal de
Ubuntu debí importar os, lo que permite escribir comandas en Python para poder pasarlas
a Ubuntu y que se puedan ejecutar desde la terminal. Esto también lo importaré para los
siguientes ejercicios

El vídeo input sería Big_Buck_Bunny.mp4, la variable cut_time serían los segundos en los
que se desee cortar (input del usuario), y el video de salida sería cut_video_12_seconds.mp4

El vídeo ya estará descargado previamente. Esto es debido a wget. Lo que hice fue descargar el
vídeo de BBB, subirlo a un directorio de Drive, copiar el enlace de descarga de Drive y finalmente
usar wget.download(URL_DESCARGA). De esta manera, solo será necesario compilar este script y todos
los vídeos se crearán. 
Para esto, primero debí instalar desde la terminal el wget
--> (pip install wget)
"""


def cut_BBB(cut_time):
    url1 = 'https://drive.google.com/uc?export=download&id=1-W3v4K9wa8yFImuH96yUqlBKkuONdeLg'
    wget.download(url1)  # Vídeo descargado -> Big_Buck_Bunny.mp4

    # cut_video_frame = str(input("Seleccione el tiempo (segundos) de corte: "))

    # El hecho de utilizar '' + cut_time + ''  permite introducir la variable de
    # input dentro de la comanda, para luego que sea leída desde la terminal de Ubuntu
    cmd = 'ffmpeg -ss 0 -i Big_Buck_Bunny.mp4 -c copy -t ' + cut_time + ' cut_video_12_seconds.mp4'
    os.system(cmd)


if __name__ == '__main__':
    cut_video_frame = str(input("Seleccione el tiempo (segundos) de corte: "))
    cut_BBB(cut_video_frame)
