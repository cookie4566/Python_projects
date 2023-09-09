# MP4 / MP3 video player app
#by Christopher Kennedy
# created 9-7-2023
from tkinter import *
from tkVideoPlayer import TkinterVideo

# Creates window and titles the window
root = Tk()
root.title = ('pymp4')
# Window size
root.geometry('1000x500')
vid = TkinterVideo(master = root, scaled = True)
vid.load(r"[ViViD REAL] Gundam AGE 3 OP.mp4")
vid.pack()

open = Button(root, text = 'open', command= root.destroy)

open.pack(fill= BOTH)

vid.play()


# intializes widow as an output
root.mainloop()