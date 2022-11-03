from pytube import Playlist
from moviepy.editor import VideoFileClip
import glob

link = Playlist(input('Insira o URL: '))

def downloader(pl):
    for video in pl.videos:
        ori_video = video.streams.get_highest_resolution()
        ori_video.download()
        titulo = video.title
        print(f'Download feito do vídeo: {titulo}')
    return titulo

def convert(titulo):
    for file in glob.glob("*.mp4"):
        print(file)
        videoclip = VideoFileClip(file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(file[:-4]+'.mp3')
        
convert(downloader(link))