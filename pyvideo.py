# MP4 / MP3 video player app
#by Christopher Kennedy
# created 9-7-2023
from tkinter import *
from tkVideoPlayer import TkinterVideo
from tkinter.filedialog import *

# Function to open mp4 files
def open():
    file = askopenfile(mode='r', filetypes=[('mp4')])
    if file is None:
        vid
        vid.load()

# Creates window and titles the window
root = Tk()
root.title = ('pymp4')
frame = Frame(root)
frame.pack()
# Window size
root.geometry('1000x500')

# Initilazing TkinterVideo and loading a test video/loading video
vid = TkinterVideo(master = root, scaled = True)
vid.load(r"[ViViD REAL] Gundam AGE 3 OP.mp4")
vid.pack(fill='both',expand='true')

# Buttons used for testing tkVideoPlayer

play = Button(root, text = "Play", command = vid.play)
pause = Button(root,text = "pause" ,command = vid.pause)

play.pack(side='left')
pause.pack(side='right')


#menu
menu = Menu(root)
fmenu = Menu(menu, tearoff=0)
menu.add_cascade(menu = fmenu, label = 'placeholder')
fmenu.add_command(label = "open",command = 'open')


# Starts video playback
vid.play()


# intializes widow as an output
root.config(menu=menu)
root.mainloop()