import machine
import time

#Configure LED pin as OUTPUT pin
led = machine.Pin("LED",machine.Pin.OUT);
button = machine.Pin(16,machine.Pin.IN,machine.Pin.PULL_UP);

while True:
    if(button.value() == 0):
        led.value(1)
    else:
        led.value(0)
