# esp32

## Setup

#### Install packages
```
$ sudo pip3 install esptool
$ sudo pip3 install rshell
```

#### Download micropython firmware
```
$ wget http://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin
```

ESP32 Firmware (GENERIC) available at http://micropython.org/download/esp32/

#### Plugin ESP32 to Linux machine
```
$ dmesg | grep ttyUSB
[17024.453233] usb 1-2: cp210x converter now attached to ttyUSB0
```

#### Read device ID
```
$ esptool.py --port /dev/ttyUSB0 flash_id
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting.....
Detecting chip type... ESP32
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 24:0a:c4:58:43:dc
Uploading stub...
Running stub...
Stub running...
Manufacturer: 5e
Device: 4016
Detected flash size: 4MB
Hard resetting via RTS pin...
```

#### Erase device
```
$ esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting........_
Detecting chip type... ESP32
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 24:0a:c4:58:43:dc
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 13.8s
Hard resetting via RTS pin...
```

#### Write to device
```
$ esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin 
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting.....
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 24:0a:c4:58:43:dc
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 1448768 bytes to 926007...
Wrote 1448768 bytes (926007 compressed) at 0x00001000 in 82.4 seconds (effective 140.7 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

#### Connect to device through rshell
```
$ rshell -p /dev/ttyUSB0
Using buffer-size of 32
Connecting to /dev/ttyUSB0 (buffer-size 32)...
Trying to connect to REPL  connected
Testing if ubinascii.unhexlify exists ... Y
Retrieving root directories ... /boot.py/
Setting time ... Oct 23, 2020 17:23:14
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 2000
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
/home/user> boards
pyboard @ /dev/ttyUSB0 connected Epoch: 2000 Dirs: /boot.py /pyboard/boot.py
/home/user> exit
```
