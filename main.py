import secretkeys as keys
from modules import udphandle as light
import time

def main():
    bulb = light.lightdata(keys.bulb_ip,keys.port,"main_bulb")
    led = light.lightdata(keys.led_ip,keys.port,"main_led")


    light.lightwhite(led,255,0,False)
    light.lightbrightness(led,100,False)
    light.lightoff(led)
    

if __name__ == "__main__":
    main()