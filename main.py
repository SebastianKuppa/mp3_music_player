from pygame import mixer
import os
import tkinter
import tkinter.font as font
from tkinter import dialog

if __name__ == '__main__':
    # creating root window
    root = tkinter.Tk()
    root.title('MP3 music player')
    # init mixer
    mixer.init()
