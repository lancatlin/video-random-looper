import subprocess

class Player:
    def __init__(self, filename):
        self.filename = filename
    
    def play(self, start, end):
        subprocess.run(['cvlc', '--fullscreen', '--play-and-exit', '--start-time={}'.format(start), '--stop-time={}'.format(end), self.filename])

if __name__ == '__main__':
    player = Player('./test.mp4')
    player.play(10, 12)
    print('exit')
    player.play(10, 12)