from pytube import Playlist
from moviepy.editor import VideoFileClip
from tkinter import *
import os
import glob

def downloader():
    pl = Playlist(entry.get())
    for video in pl.videos:
        ori_video = video.streams.get_highest_resolution()
        ori_video.download('downloads')
        title = video.title
        # print(f'Video downloaded: {title}')
    print("Downloaded!")
    convert()
    
def convert():
    mp3_dir = 'C:/Users/supor/OneDrive/Documentos/.mp3'
    for file in glob.glob("downloads/*.mp4"):
        print(file)
        videoclip = VideoFileClip(file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(file[:-4]+'.mp3')
        for file2 in os.listdir('downloads'):
            if '.mp3' in file2:
                os.rename(f"downloads/{file2}", mp3_dir + "/" + file2)
    print("Converted!")

def reencaminhar():
    mp4_dir = 'C:/Users/supor/OneDrive/Documentos/.mp4'
        
    for file in os.listdir('downloads'):
        if '.mp4' in file:
            os.rename(f"downloads/{file}", mp4_dir + "/" + file)
    print('Files transfered!')
    
window = Tk()
window.geometry('500x180')
window.title('YT Downloader')
window.configure(background='#dde')

text = Label(window, text="Insert the URL: ")
text.place(x=210, y=10)

entry = Entry(window, width=60)
entry.place(x=80,y=50)

download = Button(window, text="Download", command=downloader)
download.place(x=220,y=90)

foward = Button(window, text="Foward", command=reencaminhar)
foward.place(x=227,y=130)

window.mainloop()