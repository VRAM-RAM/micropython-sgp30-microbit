# micropython-sgp30-microbit
Minimal standalone MicroPython SGP30 driver for BBC Micro:bit with serial CSV logging and LCD display.

# Informations :

This code is intended to be imported onto a BBC MicroBIT board, which is connected to an LCD screen and an "SGP30" CO2 sensor, thanks to the Grove shield.
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
Regarding the code itself, since the source code for using the sensor was not available, I rewrote a "homemade" driver. It is not perfect but functional and
sufficient for the use we make of it.

Here is the assembly that was made: [vittascience-link](https://fr.vittascience.com/learn/tutorial.php?id=35)

Finally, if you wish to save the values into a .csv directly in your current folder, use the program ```csv_save.py```.

## Notes

This is a simple homemade driver written for educational purposes.
It is not optimized and was built because no MicroPython driver was available.
