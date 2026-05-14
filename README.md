# micropython-sgp30-microbit : a minimal SGP30 Driver for MicroPython on BBC Micro:bit
![MicroPython](https://img.shields.io/badge/MicroPython-compatible-brightgreen)
![micro:bit](https://img.shields.io/badge/BBC-microbit-yellow)
![License MIT](https://img.shields.io/badge/license-MIT-blue)

Designed for educational use:
- simple codebase
- no external dependencies (except microbit library)
- easy to modify
- compatible with LCD displays and serial CSV logging

  
# Informations :

This code is intended to be imported onto a BBC MicroBIT board, which is connected to an LCD screen and an SGP30 air quality sensor (eCO2 and TVOC), thanks to the Grove shield.
To flash the MicroBIT board, no matter which text editor you use, first activate a Python environment, then run:

```
pip install uflash pyserial
```

After that, edit the source code, then flash the board:

```
uflash captor_code.py
```

It is automatically detected and flashed when the command is executed.

Finally, to read the live values in your terminal, run:

```
sudo python3 -m serial.tools.miniterm /dev/ttyACM0 115200
```

Note: these commands work on Linux. For Mac, it is pretty much the same thing, and for Windows, it will be possible to use: [microsoft-makecode](https://www.microsoft.com/fr-fr/makecode)
Regarding the code itself, this project intentionally uses a small custom-written driver to keep the code readable and educational.

Here is the assembly that was made: [vittascience-link](https://fr.vittascience.com/learn/tutorial.php?id=35)

Finally, if you wish to save the values into a .csv directly in your current folder, use the program ```csv_save.py```.

## Notes

This is a simple homemade driver written for educational purposes.
Although other MicroPython implementations exist, this project includes a minimal custom driver adapted for my Micro:bit setup.
