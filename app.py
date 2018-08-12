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
    currFrame = 0
    frames = None
    selfPhoto = None

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
        self.currFrame += 1

        self.photo = PIL.ImageTk.PhotoImage(image=self.frames[self.currFrame])

        self.videoCanvas.itemconfig(self.canvas_id, image=self.photo, anchor=NW)
        print(self.videoCanvas.itemcget(self.canvas_id, 'image'))

    def __init__(self):
        args = sys.argv

        videoPath = args[1]

        self.frames = self.createImages(videoPath)

        self.window = Tk()
        self.window.title('Media Player')

        width, height = self.frames[self.currFrame].size

        self.videoCanvas = Canvas(self.window, width=width, height=height)
        self.videoCanvas.pack()

        nextBtn = Button(self.window, text="Next Frame", command=self.nextFrame)
        nextBtn.pack(side="bottom")

        quitBtn = Button(self.window, text="Quit", command=self.window.destroy)
        quitBtn.pack(side="bottom")

        self.photo = PIL.ImageTk.PhotoImage(image=self.frames[self.currFrame])

        self.canvas_id = self.videoCanvas.create_image(0, 0, image=self.photo, state='normal', anchor=NW)

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
