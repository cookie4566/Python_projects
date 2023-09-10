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
# Initilazing TkinterVideo and loading a test video/loading video
vid = TkinterVideo(master = root, scaled = True)
vid.load(r"[ViViD REAL] Gundam AGE 3 OP.mp4")
vid.pack()


# Buttons used for testing tkVideoPlayer

play = Button(root, text = "Play", command = vid.play)
pause = Button(root,text = "pause" ,command = vid.pause)

play.pack()
pause.pack()

#menu
menu = Menu(root)
fmenu = Menu(menu, tearoff=0)
menu.add_cascade(menu = fmenu, label = 'placeholder')
fmenu.add_command(label = "open",command = root.destroy)


# Starts video playback
vid.play()


# intializes widow as an output
root.config(menu=menu)
root.mainloop()