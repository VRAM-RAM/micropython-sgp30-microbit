"""

File for saving the values into a CSV file. To use it, please change the port, and execute :

sudo python3 csv_save.py

To stop the save, simply do a Keyboard Interrupt (Ctrl + C)
"""

import serial
import csv
import os
import sys
import time

CONFIG = {
    "port": "/dev/ttyACM0",         
    "baudrate": 115200,      
    "csv_file": "data_microbit.csv"  #TO CHANGE WITH YOUR OWN NAME
}

def main():
    print(f"Connection to {CONFIG['port']}...")
    try:
        ser = serial.Serial(CONFIG['port'], CONFIG['baudrate'], timeout=1)
        time.sleep(2) 
        print("Connected")
    except serial.SerialException as e:
        print(f"Serial error : {e}")
        print("Verify the port")
        sys.exit(1)

    file_exists = os.path.isfile(CONFIG['csv_file'])
    with open(CONFIG["csv_file"], "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["time_ms", "co2_ppm", "tvoc_ppb"])

        try:
            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) == 3:
                    try:
                        t_ms = int(parts[0])
                        co2 = int(parts[1])
                        tvoc = int(parts[2])
                        
                        writer.writerow([t_ms, co2, tvoc])
                        f.flush()  
                        
                        print(f"[{t_ms}ms] CO2: {co2} ppm | TVOC: {tvoc} ppb")
                    except ValueError:
                        pass  
        except KeyboardInterrupt:
            print("\nStopping save...")
        finally:
            if ser.is_open:
                ser.close()
            print(f"Saved at : {os.path.abspath(CONFIG['csv_file'])}")

if __name__ == "__main__":
    main()
