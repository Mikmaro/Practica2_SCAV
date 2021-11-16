# Mario Fernández
# Exercise 4

"""
Ambas funciones encontré los códigos por internet, donde la primera transforma de stereo
a mono, y el segundo cambia el audio codec
"""
import os


def stereo_to_mono():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -ac 1 MONO_cut_video_12_seconds.mp4 '
    os.system(cmd)


def change_audio_codec():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -vcodec copy -acodec mp3 mp3_cut_video_12_seconds.mp4 '
    os.system(cmd)


if __name__ == '__main__':
    stereo_to_mono()
    change_audio_codec()
