from pytube import Playlist
def yt_playlist():
    link = input("link: ")
    yt_playlist = Playlist(link)
    for video in yt_playlist.videos:
        video.streams.get_highest_resolution().download("F:\\N3")
        print("Downloaded: ", video.title)
    print("Finished")