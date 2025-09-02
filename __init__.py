import requests
import os
import ctypes
import vlc

from time import sleep
from yt_dlp import YoutubeDL


class Play_DLL:

    def __init__(self):

        # Get the absolute path to Play_DLL folder
        self.currentDir = os.path.dirname(os.path.abspath(__file__))

        # Defining vlc files path
        self.vlcPath = os.path.join(self.currentDir, "vlc")

        # Add to system path at runtime
        os.environ["PATH"] = self.vlcPath + os.pathsep + os.environ["PATH"]

        # Load the DLL manually. This was done to avoid the error Libvlc.dll not found.
        ctypes.CDLL(os.path.join(self.vlcPath, "libvlc.dll"))

    def url_extracter(self, song_name: str) -> str:
        """
        Function to find the song url from the entered youtube URL.
        """

        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "default_search": "ytsearch",
            "noplaylist": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(song_name, download=False)
            # If it's a search result, extract the first entry
            if "entries" in info:
                info = info["entries"][0]

        return info["url"]

    def get_yt_song_url(self, query):
        """
        Function to find YouTube video URL of the Song requested.
        """

        url = "https://www.youtube.com/results?q=" + query + " song lyrics"

        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')

        for i in lst:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH":
                break
        if lst[count - 5] == "/results":
            raise Exception("No video found.")

        return "https://www.youtube.com" + lst[count - 5]

    def play_by_song_url(self, url):
        """
        Function to play song from video/song URL
        """

        try:

            self.player.stop()  # stops the player if already playing

        except:
            pass

        self.player = vlc.MediaPlayer(url)

        self.player.play()  # plays the song
        sleep(1)
        while self.player.is_playing:
            sleep(1)
        else:
            self.player.stop()

    def play_by_yt_url(self, yt_url):
        """Function to play song from youtube video URL"""

        self.play_by_song_url(
            self.url_extracter(yt_url)
        )  # extracts the song url from the youtube url and feeds to play_by_song_url function

    def play_by_songName(self, song_name):
        """
        Function which will take song name as argument and then find the YouTube video url of that song;
        After that it find the video URL of the Song then play it.
        """

        url_of_song = (self.get_yt_song_url(song_name)).split("""\\""")[0]
        self.play_by_yt_url(url_of_song)

    def play_by_file(self, file_path):
        """Can play a song/audio from a file path"""

        self.play_by_song_url(file_path)

    # ========= All the pause, resume, rewind etc type of functions ===== #

    def pause_resume_song(self):
        """
        Function to pause or resume the playing song.
        """
        if self.player != "":
            self.player.pause()

    def seek(self, pos):
        """Seeks the player to a specific position"""

        # here in the arguments we are supposed to give the seconds to which we have to seek.
        # lIKE IF WE HAVE TO SEEK TO 20 SECONDS THEN WE HAVE TO GIVE 20 IN THE ARGUMENTS

        self.player.set_position(pos)
