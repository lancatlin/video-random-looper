from vlc import Instance, libvlc_set_fullscreen
import time
import os
import random


START = 0
MIDDLE = 15
END = 30


class VLC:
    def __init__(self, filename):
        self.Player = Instance('--fullscreen').media_player_new(filename)
        libvlc_set_fullscreen(self.Player, True)

    def loop(self):
        self.play()
        while True:
            start = random.randint(START, MIDDLE)
            end = random.randint(MIDDLE, END)
            self.seek(start)
            print(start, end)
            time.sleep(end - start)

    def play(self):
        self.Player.play()

    def seek(self, position):
        self.Player.set_time(position * 1000)

    def stop(self):
        self.Player.stop()


if __name__ == '__main__':
    player = VLC('test.mkv')
    try:
        player.loop()
    except KeyboardInterrupt:
        player.stop()
        print('exit')
