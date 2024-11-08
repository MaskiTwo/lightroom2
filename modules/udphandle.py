import socket

class lightdata:
    name = ""
    ip = ""
    port = 0
    state = "true"

    brightness = 0
    
    red = 0
    green = 0
    blue = 0

    cool_white = 0
    warm_white = 0

    def __init__(self,ip:str,port:int,name:str="unnamed"):
        self.ip= ip
        self.port = port
        self.name = name
    
    def lightdata(self):
        print(f"Data of {self.name} : {self.ip}:{self.port}")

    def switch(self,type:str="on"):
        if type == "on":
            self.state = "true"
        elif type == "off":
            self.state = "false"
        else:
            raise TypeError("You can only switch the light on/off!")

    def messageBuilder(self):
        # making the json structure for the udp message
        message = {"method":"setPilot","params":{}}
        message["params"]["state"] = self.state
        if self.brightness != 0:
            message["params"]["dimming"] = self.brightness
        if self.red != 0:
            message["params"]["r"] = self.red
        if self.green != 0:
            message["params"]["g"] = self.green
        if self.blue != 0:
            message["params"]["b"] = self.blue
        if self.cool_white != 0:
            message["params"]["c"] = self.cool_white
        if self.warm_white != 0:
            message["params"]["w"] = self.warm_white

        # correcting forrmating errors
        newmessage = str(message)
        newmessage = newmessage.replace("'",'"')
        newmessage = newmessage.replace(" ",'')
        newmessage = newmessage.replace('"true"','true')
        newmessage = newmessage.replace('"false"','false')
        return newmessage

def push_udp(data:lightdata):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    message = data.messageBuilder()
    sock.sendto(message.encode(), (data.ip, data.port))

def lightoff(data:lightdata,push:bool=True):
    data.switch("off")
    if push == True:
        push_udp(data)

def lighton(data:lightdata,push:bool=True):
    data.switch("on")
    if push == True:
        push_udp(data)

def lightcolor(data:lightdata,red:int,green:int,blue:int,push:bool=True):
    checker = [red,green,blue]
    for x in checker:
        if x < 0:
            raise ValueError("RGB Value cannot be negative!")

    data.red = red
    data.green = green
    data.blue = blue

    if push == True:
        push_udp(data)

def lightbrightness(data:lightdata,brightness:int,push:bool=True):
    if brightness < 0:
        raise ValueError("Brightness value cannot be negative!")
    
    data.brightness = brightness

    if push == True:
        push_udp(data)

def lightwhite(data:lightdata,cool:int,warm:int,push:bool=True):
    if cool < 0 or warm < 0:
        raise ValueError("Cool or Warm value cannot be negative!")
    
    data.cool_white = cool
    data.warm_white = warm

    if push == True:
        push_udp(data)
