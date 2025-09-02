# Play_DLL

Play_DLL is a python and vlc based music player that can stream any song directly from the web

# Functions
- **🎵Playing song directly from song name** 
- **▶Playing songs directly from youtube URL**
- **📂Playing songs directly from files**
- **⏸️Seeking, pause, resume functionality**
- **</>No console output**
# Usage
```python
import Play_DLL

player = Play_DLL.Play_DLL()
player.play_by_songName("Blinding lights")
```

### Pause/Resume
Resumes or pauses the song.
```python
player.pause_resume_song()
```

### Seeking

```python
player.seek(12) # <-- In seconds, make sure it is less than the duration 
```

# Inner Logic

- **Parsing the youtube results, after searching the song name using *requests***

- **Using the topmost result's youtube URL, the URL of the best audio stream is derived using *yt_dlp***

- **The URL is then streamed by python-vlc**
