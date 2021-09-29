import pyautogui as pt
from time import sleep

class GuiCommands:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def navigate(self,speed):
        position = pt.locateOnScreen("bookmark.png",confidence = 0.8)
        self.x = position[0] - 540
        self.y = position[1] + 10
        pt.moveTo(self.x,self.y,duration = speed)
        sleep(0.3)

commands = GuiCommands(0,0)

for i in range(20):
    try:
        commands.navigate(1)
        if pt.pixelMatchesColor(pt.position().x,pt.position().y,(237,73,86), tolerance=10):
            pt.scroll(500)
            sleep(0.3)
        else:
            pt.click()
            sleep(0.3)

    except Exception as e:
        print(e)
        pt.scroll(500)
        sleep(0.3)
