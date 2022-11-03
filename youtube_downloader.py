from pytube import YouTube

link = input('Insira o URL: ')

yt = YouTube(link)

print(f"Título: {yt.title}")

res_yt = yt.streams.get_highest_resolution().download()