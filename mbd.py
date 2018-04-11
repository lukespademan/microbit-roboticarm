from microbit import *
import radio

radio.on()


while True:
    data = radio.receive()
    if data:
        print(data)
