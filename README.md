\# Rhino PS2 Controller to Xbox Controller Adapter



A Python-based adapter that converts a wireless PS2 controller connected through a Rhino RKI-1580 controller board into a virtual Xbox 360 controller for Windows.



This project was developed by reverse engineering the serial protocol output by the Rhino board used in the ESVC (Electric Solar Vehicle Championship) Junior robotics kit.



\---



\## Features



\- Wireless PS2 controller support

\- Virtual Xbox 360 controller using ViGEm

\- Supports:

&#x20; - Left Analog Stick

&#x20; - Right Analog Stick

&#x20; - D-Pad

&#x20; - Cross (X)

&#x20; - Circle (O)

&#x20; - Square

&#x20; - Triangle

&#x20; - L1 / R1

&#x20; - L2 / R2 (Triggers)

&#x20; - Start

&#x20; - Select

\- Automatic button press/release handling

\- Dead-zone filtering

\- Ignores duplicate serial packets for improved performance

\- Clean controller shutdown



\---



\## Hardware Required



\- Rhino RKI-1580 Controller Board

\- Rhino Wireless PS2 Receiver

\- Rhino Wireless PS2 Controller

\- USB cable for Rhino Board

\- Windows PC



\---



\## Software Requirements



Python 3.10+



Packages:



```bash

pip install pyserial vgamepad

```



ViGEmBus Driver:



https://vigembusdriver.com/



Install the driver before running the program.



\---



\## Folder Structure



```

RhinoController/

│

├── main.py

├── parser.py

├── mapper.py

├── calibrate.py

├── requirements.txt

├── README.md

└── Start\_Controller.bat

```



\---



\## Installation



Clone or download the project.



Install dependencies:



```bash

pip install -r requirements.txt

```



or



```bash

pip install pyserial vgamepad

```



Install ViGEmBus Driver.



Connect the Rhino board.



Turn on the controller.



Run:



```bash

python main.py

```



\---



\## How It Works



```

Wireless PS2 Controller

&#x20;         │

&#x20;         ▼

&#x20;Rhino Wireless Receiver

&#x20;         │

&#x20;         ▼

&#x20;    Rhino RKI-1580

&#x20;         │

&#x20;    USB Serial (57600)

&#x20;         │

&#x20;         ▼

&#x20;     Python Parser

&#x20;         │

&#x20;         ▼

&#x20; Virtual Xbox Controller

&#x20;         │

&#x20;         ▼

&#x20;        Windows

```



The Rhino board continuously sends controller state over serial.



Python converts these packets into Xbox controller events using the ViGEm virtual controller driver.



\---



\## Button Mapping



| PS2 Controller | Xbox Controller |

|---------------|-----------------|

| Cross (X) | A |

| Circle (O) | B |

| Square | X |

| Triangle | Y |

| L1 | Left Shoulder |

| R1 | Right Shoulder |

| L2 | Left Trigger |

| R2 | Right Trigger |

| Start | Start |

| Select | Back |

| D-Pad | D-Pad |

| Left Stick | Left Stick |

| Right Stick | Right Stick |



\---



\## Serial Protocol



Baud Rate



```

57600

```



Typical Packet



```

65 127 127 127 127

```



Packet Format



```

HEADER LX LY RX RY BUTTONS...

```



Example



```

65 255 127 127 127 RG

```



Meaning



```

LX = 255

LY = 127

RX = 127

RY = 127

Button = Right D-Pad

```



\---



\## Supported Buttons



\- A (Triangle)

\- X (Cross)

\- O (Circle)

\- D (Square)

\- UP

\- DN

\- LF

\- RG

\- L1

\- L2

\- R1

\- R2

\- ST (Start)

\- SL (Select)



\---



\## Known Limitations



\- Controller vibration (rumble) is currently unsupported.

\- L3/R3 support depends on the Rhino firmware.

\- Requires the Rhino board to remain connected while playing.

\- Windows only.



\---



\## Troubleshooting



\### Controller not detected



\- Verify ViGEmBus is installed.

\- Check Device Manager for the CH340 USB Serial device.

\- Verify the correct COM port.



\---



\### No controller input



Check:



\- Receiver powered

\- Controller batteries

\- Controller connected to receiver

\- Baud rate is 57600



\---



\### Buttons stuck



Restart:



```

Ctrl + C

```



The controller automatically resets on exit.



\---



\## Future Improvements



\- GUI using PyQt6

\- Automatic controller calibration

\- Configurable button mapping

\- Profile switching

\- Build standalone executable

\- Auto-start with Windows

\- Configuration file support



\---



\## Credits



Developed by



\*\*Nitin Prasad Singh\*\*



Reverse engineering and software development completed using Python and ViGEm.



Special thanks to OpenAI ChatGPT for assisting in protocol analysis, debugging, and implementation.



\---



\## License



This project is provided for educational and personal use.



No affiliation with Rhino Robotics or ESVC.

