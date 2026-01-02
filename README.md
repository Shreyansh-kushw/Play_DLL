# 🎧 Play_DLL

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL-green.svg)](./LICENSE)
[![VLC](https://img.shields.io/badge/VLC-Required-orange.svg)](https://www.videolan.org/vlc/)

**Play_DLL** is a lightweight Python library built on **VLC** that allows you to **stream and control music directly from the internet** with just a few lines of code.

---

## ✨ Features

* 🎵 **Play songs directly from song name**
* ▶️ **Play songs directly from YouTube URL**
* 📂 **Play songs directly from local files**
* ⏸️ **Pause, Resume & Seek functionality**
* 🧼 **No console output clutter**

---

## 🚀 Installation

```bash
pip install python-vlc yt-dlp requests
```

(You can also clone this repo to access the full implementation.)

```bash
git clone https://github.com/yourusername/Play_DLL.git
cd Play_DLL
```

---

## 🧪 Usage Example

```python
import Play_DLL

player = Play_DLL.Play_DLL()
player.play_by_songName("Blinding Lights")
```

### ⏸ Pause / Resume

```python
player.pause_resume_song()
```

### ⏩ Seek

```python
player.seek(12)  # in seconds (must be less than total duration)
```

---

## 🧠 Inner Logic

* Parses YouTube search results using **`requests`**
* Fetches the **top audio stream URL** with **`yt_dlp`**
* Streams the audio using **`python-vlc`**

---

## 📂 Project Structure

```
Play_DLL/
│── Play_DLL.py        # Main player module
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```

---

## 📝 License

This project is licensed under the [GPL-3.0 License](./LICENSE).

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature
