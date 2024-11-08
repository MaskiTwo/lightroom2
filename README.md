# Room Light Controller

A self-made library to control the lights in my room, specifically Philips Wiz lights using UDP.

## Introduction
This project provides a Python library to programmatically control Philips Wiz smart lights in my room using the UDP protocol. The library allows me to turn the lights on/off, adjust brightness, change colors, and integrate with other devices in my room.

## Features
- **Light Control**: Turn lights on/off, adjust brightness, and change color.
- **UDP Communication**: Communicates with the Wiz lights using the UDP protocol.
- **Easy-to-use API**: Provides a simple and intuitive API to interact with the lights.

## Installation
To use the Room Light Controller, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/MaskiTwo/lightroom2.git
   ```
2. Change to the project directory:
   ```
   cd room-light-controller
   ```
3. Install the required dependencies: (will do later)
   ```
   pip install -r requirements.txt
   ```

## Usage
Here's an example of how to use the Room Light Controller library:

```python
from modules import udphandle as light

# Create a light instance
led = light.lightdata(keys.led_ip,keys.port,"main_led") # insert your own ip and port
# the "main_led" is just naming and is optional

# Display the name, ip, and port of the light instance
led.lightdata()

# Turn the light on
light.lighton(led)

# Set the light color to red
light.lightcolor(led,255,0,0)

# Adjust the brightness to 50%
light.lightbrightness(led,50)
```

For more detailed usage examples and documentation, please refer to the source code itself (there isnt a wiki yet).

## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or contact me directly. Suggestions and ideas are always welcome!

## License
This project is licensed under the [MIT License](LICENSE).
