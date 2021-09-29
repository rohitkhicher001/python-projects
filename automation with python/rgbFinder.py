import pyautogui as pt
from time import sleep

while True:
    try:

        pos = pt.position()                                       #to get position of current pointer position
        print(pos,  pt.pixel(pos[0],pos[1]))                      #to  get color of position we are hovering
        sleep(1)                                                  #for delay
        if pos[0] == 0:
            break

    except Exception:
        pass
