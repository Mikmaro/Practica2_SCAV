# Mario Fernández
# Exercise 3

"""
El video input se llama cut_video_12_seconds.mp4
"""
import os


def resize_720p():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB720p.mp4 '

    os.system(cmd)


def resize_480p():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 BBB480p.mp4 '

    os.system(cmd)


def resize_360_240():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -s 360x240 -c:a copy BBB360_240.mp4 '

    os.system(cmd)


def resize_160_120():
    cmd = ' ffmpeg -i cut_video_12_seconds.mp4 -s 160x120 -c:a copy BBB160_120.mp4 '
    os.system(cmd)


if __name__ == '__main__':
    resize_720p()
    resize_480p()
    resize_360_240()
    resize_160_120()
