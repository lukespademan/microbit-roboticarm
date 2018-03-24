from microbit import *
import radio


radio.on()

x_image = Image("90009:"
                "09090:"
                "00900:"
                "09090:"
                "90009:")


images = {
        "u": Image.ARROW_N,
        "d": Image.ARROW_S,
        "l": Image.ARROW_W,
        "r": Image.ARROW_E,
        "f": x_image
}

def get_dir():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    abs_x = abs(x)
    abs_y = abs(y)
    amount = 300
    if abs_x > abs_y:
        if x > amount:
            return "r"
        if x < -amount:
            return "l"
    elif abs_y > abs_x:
        if y > amount:
            return "d"
        if y < -amount:
            return "u"
    return "f"

while True:
    d = get_dir()
    to_add = "1" if button_a.is_pressed() else "0"
    radio.send(d + to_add)
    display.show(images[d])
    sleep(250)
