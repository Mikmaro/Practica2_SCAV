# Mario Fernández
# Exercise 3

"""
El video input se llama cut_video_12_seconds.mp4
"""
import os
import wget


def resize():
    url1 = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url1)  # Vídeo descargado -> cut_video_12_seconds.mp4
    # resize_720p:
    cmd1 = 'ffmpeg -i cut_video_12_seconds.mp4 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB720p.mp4'

    os.system(cmd1)

    # resize_480p:
    cmd2 = ' ffmpeg -i cut_video_12_seconds.mp4 -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB480p.mp4 '

    os.system(cmd2)

    # resize_360_240:
    cmd3 = 'ffmpeg -i cut_video_12_seconds.mp4 -s 360x240 -c:a copy BBB360_240.mp4'

    os.system(cmd3)

    # resize_160_120:
    cmd4 = 'ffmpeg -i cut_video_12_seconds.mp4 -s 160x120 -c:a copy BBB160_120.mp4'
    os.system(cmd4)


if __name__ == '__main__':
    resize()
