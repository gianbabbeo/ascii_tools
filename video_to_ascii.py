
###################################
### video from argv
### convert in ascii art
### creates .ascii
### ---
### via argv -play
### plays the ascii video
###################################

from sys import argv
import math
import cv2

CHARACTERS = (' ', '.', '°', '*', 'o', 'O', '#', '@')
MAX_INTENSITY = 255*4

def main() -> None:
    #apro video 
    video_name = argv[1]
    video = cv2.VideoCapture(video_name)

    #prendo dati da header
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = float(video.get(5))

    #creo l'output ascii
    ascii_name = video_name + '.ascii'
    ascii = open(ascii_name, 'wb')

    #normalizzo frame rate
    frame_rate = math.ceil(frame_rate)
    if frame_rate > 255:
        frame_rate = 255
    elif frame_rate < 1:
        frame_rate = 1
    frame_rate = bytes([frame_rate])

    #scrivo header
    ascii.write(
        int.to_bytes(width, 2, 'big') +
        int.to_bytes(height, 2, 'big') +
        frame_rate +
        int.to_bytes(frame_count, 8, 'big')
    )

    #loop conversione
    while video.isOpened():
        #per ogni frame...
        ret, frame = video.read()
        #...se frame vuoto...
        if not ret:
            #...esci...
            break

        #...altrimenti...
        #### CONVERSIONE E SCRITTURA


if __name__ == '__main__':
    main()