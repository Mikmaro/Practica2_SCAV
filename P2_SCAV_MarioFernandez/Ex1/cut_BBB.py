# Mario Fernández
# Exercise 1

"""
En el terminal, debí hacer primero-->     pip install --trusted pypi.python.org moviepy

Una vez hecho esto, encontré una líndea por internet que hacía exactamente lo
que se nos pedía, así que compilando este script desde la terminal se creó el vídeo
con el tiempo de corte deseado (para cambiar este corte se debe modificar la variable
cut_video_frame)
"""

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def cut_BBB(cut_time):
    ffmpeg_extract_subclip("Big_Buck_Bunny.mp4", 0, cut_time, targetname="cut_video_12_seconds.mp4")


if __name__ == '__main__':
    cut_video_frame = 12
    cut_BBB(cut_video_frame)
