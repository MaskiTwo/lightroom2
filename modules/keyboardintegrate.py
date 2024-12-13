import keyboard
from modules import udphandle as light

class InputHandler:
    BrightnessControl = True
    ColorShiftControl = True

    def ToggleBrightnessControl(self,switch:bool):
        self.BrightnessControl = switch
        

    def ToggleColorShiftControl(self,switch:bool):
        self.ColorShiftControl = switch



def left_BrightnessControl(data:light.lightdata):
    bright = data.brightness #- step
    if bright <= 0:
        #light.lightoff(data)
        light.lightbrightness(data,1)
    else:
        light.lightbrightness(data,bright)

def right_BrightnessControl(data:light.lightdata):
    bright = data.brightness #+ step
    if bright >= 100:
        light.lightbrightness(data,100)
    else:
        light.lighton(data,False)
        light.lightbrightness(data,bright)
    print("right")

def left(event):
    left_BrightnessControl()

def right(event):
    right_BrightnessControl()

    # keyboard.on_press_key("f12",f12_press)
    # keyboard.on_release_key("f12", f12_release)

#---------------------------------

def KeyboardIntegrate(data:light.lightdata,key:InputHandler):

    if key.BrightnessControl == True:
        keyboard.on_release_key("left", left)
        keyboard.on_release_key("right", right)

    if key.ColorShiftControl == True:
        pass

    print("esc to exit")
    keyboard.wait('esc') 
    pass