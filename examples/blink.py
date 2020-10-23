import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

print("Start blinking")
try:
    while True:
        print("LED ON")
        led.value(1)
        time.sleep(.5)
        print("LED OFF")
        led.value(0)
        time.sleep(.5)
except KeyboardInterrupt:
    print("Stop blinking")
    led.value(0)
