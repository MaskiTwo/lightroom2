import socket

class data:
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

def push_udp(data:data):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    message = data.messageBuilder()
    sock.sendto(message.encode(), (data.ip, data.port))


def lightoff(data:data):
    data.switch("off")
    push_udp(data)

def lighton(data:data):
    data.switch("on")
    push_udp(data)

def lightcolor(type:str,):
    pass