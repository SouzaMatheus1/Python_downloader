from pytube import YouTube
from playlist_yt_downloader import *

link = input('Insert the URL: ')

yt = YouTube(link)

res_yt = yt.streams.get_highest_resolution().download('single videos')

print(f"Downloaded video: {yt.title}")