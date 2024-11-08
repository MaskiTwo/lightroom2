import secretkeys as keys
from modules import udphandle as light
import time

def main():
    bulb = light.data(keys.bulb_ip,keys.port,"main_bulb")
    led = light.data(keys.led_ip,keys.port,"main_led")
    
    for x in range(1,4):
        light.lighton(led)
        time.sleep(0.1)
        light.lightoff(led)
        print(x)
        time.sleep(0.1)
    

if __name__ == "__main__":
    main()