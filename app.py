from tkinter import *
import PIL.Image, PIL.ImageTk
from matplotlib import cm
import cv2
import sys
import numpy as np
import json
import os
import time


class mediaPlayer:
    def createImages(self, filename):
        capture = cv2.VideoCapture(filename)

        if(capture.isOpened() == False):
            print('File could not be opened.')

        frames = []
        while(capture.isOpened()):
            ret, frame = capture.read()

            if ret == True:
                img = PIL.Image.fromarray(frame.astype(np.uint8))
                frames.append(img)
            else:
                break

        return frames

    def nextFrame(self):
        print('next')

    def __init__(self):
        args = sys.argv

        videoPath = args[1]

        # frames = self.createImages(videoPath)

        self.window = Tk()
        self.window.title('Media Player')

        # width, height = frames[0].size

        # videoCanvas = Canvas(self.window, width = width, height = height)
        # videoCanvas.pack()

        pauseBtn = Button(self.window, text="Pause", command=self.nextFrame)
        pauseBtn.pack(side="bottom")

        quitBtn = Button(self.window, text="Quit", command=self.window.destroy)
        quitBtn.pack(side="bottom")

        # photo = PIL.ImageTk.PhotoImage(image = frames[0])
        # item = videoCanvas.create_image(0, 0, image=photo, anchor=NW)

        self.window.mainloop()

player = mediaPlayer()


# i = 0
# for frame in frames:
#     photo = PIL.ImageTk.PhotoImage(image = frames[i])
#
#     videoCanvas.itemconfig(item, photo)
#
#     time.sleep(.25)
#     print(i)
#     i += 1
