import secretkeys as keys
from modules import udphandle as light
from modules import keyboardintegrate as keyboard

def main():
    bulb = light.lightdata(keys.bulb_ip,keys.port,"main_bulb")
    led = light.lightdata(keys.led_ip,keys.port,"main_led")

    keyboard.KeyboardIntegrate(led,5)
    

if __name__ == "__main__":
    main()