
from microbit import i2c, sleep, display, Image, running_time

def _crc8(data, crc_init=0xFF):
    crc = crc_init
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ 0x31) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
    return crc

class SGP30:
    def __init__(self, addr=0x58):
        self.addr = addr
        self.init_air_quality()

    def _write_cmd(self, cmd):
        i2c.write(self.addr, cmd)

    def init_air_quality(self):
        self._write_cmd(b'\x20\x03')
        sleep(15000) #It is recommended to use at least 15 seconds. I recommend you 1 or 2 minutes

    def _read_with_crc(self, cmd, value_index):
        self._write_cmd(cmd)
        sleep(24)

        data = i2c.read(self.addr, 6)

        if len(data) != 6:
            raise RuntimeError("I2C read error")

        msb = data[value_index]
        lsb = data[value_index + 1]
        crc_received = data[value_index + 2]

        crc_calculated = _crc8([msb, lsb])

        if crc_calculated != crc_received:
            raise RuntimeError("CRC error")

        return (msb << 8) | lsb

    def eCO2(self):
        return self._read_with_crc(b'\x20\x08', 0)

    def TVOC(self):
        return self._read_with_crc(b'\x20\x08', 3)

print("Initialization of the SGP30...")
sensor = SGP30()
print("Initialization done")

def air_quality(co2):
    if co2 < 800:
        return Image.HAPPY #don't really trust this : it doesn't really reflect the reality (HAPPY can means 200 ppm or 800ppm)
    elif co2 < 1200:
        return Image.MEH
    else:
        return Image.SAD

while True:
    try:
        co2 = sensor.eCO2()
        tvoc = sensor.TVOC()

        t_ms = running_time()

        print("{},{},{}".format(t_ms, co2, tvoc)) #Formated for CSV saving

        display.show(air_quality(co2))
        sleep(1000)
        display.scroll(str(co2) + "ppm")

    except Exception as e:
        print("ERR: {}".format(e))
        display.show(Image.SKULL)
        sleep(2000)

    sleep(1000)
