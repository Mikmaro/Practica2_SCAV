# Mario Fernández
# Exercise 4

"""
Ambas funciones encontré los códigos por internet, donde la primera transforma de stereo
a mono, y el segundo cambia el audio codec
"""
import os
import wget


def stereo_to_mono():
    url1 = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'
    wget.download(url1)  # Vídeo descargado para input -> cut_video_12_seconds.mp4
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -ac 1 MONO_cut_video_12_seconds.mp4'
    os.system(cmd)  # Vídeo ouptut ->  MONO_cut_video_12_seconds.mp4


def change_audio_codec():
    # Se utiliza el mismo vídeo de antes como input -> cut_video_12_seconds.mp4
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -vcodec copy -acodec mp3 mp3_cut_video_12_seconds.mp4'
    os.system(cmd)  # Vídeo ouptut ->  mp3_cut_video_12_seconds.mp4


if __name__ == '__main__':
    stereo_to_mono()
    change_audio_codec()
