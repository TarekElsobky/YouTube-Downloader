from pytube import YouTube
from termcolor import colored
from os import getlogin, chdir

youtube_url = input(colored("Enter youtube link >> ", "yellow"))
yt = YouTube(youtube_url)

choice = input(colored("Type \"1\" for video and \"2\" for audio >> ", "yellow"))

if choice == "1":
    chdir(f"C:\\Users\\{getlogin()}\\Videos")
    streams = yt.streams.filter(only_video=True, mime_type="video/mp4")
    c = 1
    itags = []
    for stream in streams:
        itags.append(str(stream).split(" ")[1].split("\"")[1])
    for stream in streams:
        print(colored(f"{c} : " + str(stream).split(" ")[3].split("\"")[1], "yellow"))
        c += 1
    quality = int(input(colored("Select quality >> ", "yellow")))
    stream = yt.streams.get_by_itag(itags[quality - 1])
    stream.download(filename=f"{yt.title}.mp4")
    print(colored(f"Video saved to : C:\\Users\\{getlogin()}\\Videos", "green"))

if choice == "2":
    chdir(f"C:\\Users\\{getlogin()}\\Music")
    streams = yt.streams.filter(only_audio=True, mime_type="audio/mp4")
    c = 1
    itags = []
    for stream in streams:
        itags.append(str(stream).split(" ")[1].split("\"")[1])
    for stream in streams:
        print(colored(f"{c} : " + str(stream).split(" ")[3].split("\"")[1], "yellow"))
        c += 1
    quality = int(input(colored("Select quality >> ", "yellow")))
    stream = yt.streams.get_by_itag(itags[quality - 1])
    stream.download(filename=f"{yt.title}.mp3")
    print(colored(f"Audio saved to : C:\\Users\\{getlogin()}\\Music", "green"))
