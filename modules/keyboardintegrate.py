import keyboard
from modules import udphandle as light

def brightnesscontrol(data:light.lightdata,step:int=10):
    def left_BrightnessControl():
        bright = data.brightness - step
        if bright <= 0:
            #light.lightoff(data)
            light.lightbrightness(data,1)
        else:
            light.lightbrightness(data,bright)

    def left(event):
        left_BrightnessControl()

    def right_BrightnessControl():
        bright = data.brightness + step
        if bright >= 100:
            light.lightbrightness(data,100)
        else:
            light.lighton(data,False)
            light.lightbrightness(data,bright)
        print("right")

    def right(event):
        right_BrightnessControl()


    keyboard.on_release_key("left", left)
    keyboard.on_release_key("right", right)


    print("esc to exit")
    keyboard.wait('esc') 

def colorcontrol(data:light.lightdata):
    f12held = False

    def f12_press(event):
        f12held = True
        print("f12p")
    
    def f12_release(event):
        f12held = False
        print("f12r")

    keyboard.on_press_key("f12",f12_press)
    keyboard.on_release_key("f12", f12_release)