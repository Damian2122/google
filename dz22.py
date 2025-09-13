from numpy import *
import pyautogui
from PIL import ImageGrab, ImageOps
import time
class DinoBot:
    def __init__(self, replaybtn, dino):
        print("Initializing DinoBot...for Damian")
        self.replaybtn = replaybtn #435 464 ніс 200 271
        self.dino = dino
    def restartgame(self):
        pyautogui.click(self.replaybtn)
    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')
    def grabImage(self):
        box = (self.dino [0] + 35, self.dino [1], self.dino [0] + 75, self.dino [1] + 30)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale (image)
        a = array(grayImage.getcolors())
        return a.sum()
#1447
    def start(self):
        self.restartgame()
        while True:
            print(self.grabImage())
            if self.grabImage() != 1447:
                self.jump()
def main():
    bot = DinoBot ((640, 500    ),(381, 506    ))
    bot.start()

if __name__ == '__main__':
    main()