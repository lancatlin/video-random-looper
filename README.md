# Video Random Looper

## Install

Clone this repository

Install vlc and python-vlc

```
sudo apt install vlc
pip3 install python-vlc
```

## Usage

Put your video in the same directory
Set the variables in looper.py

```
FILENAME = 'test.mp4'   # Put your video path here
START = 0               # Start second 
MIDDLE = 15             # Middle second
END = 30                # End second
```

Play the video

```
python3 looper.py
```

It will play in fullscreen. ALT + TAB to turn back and use CTRL + C to stop it.