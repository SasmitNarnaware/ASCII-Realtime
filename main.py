import cv2
import os
import time
import numpy as np

from colorama import init, Fore, Style

init()

ASCII_GRADIENTS = {
    "smooth": " .:-=+*#%@",
    "blocks": " ░▒▓█",
    "detailed": " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
}

COLOR_MODES = {
    "white": Style.RESET_ALL,
    "green": Fore.GREEN,
    "red": Fore.RED,
    "cyan": Fore.CYAN,
    "yellow": Fore.YELLOW,
}

#change gradient_name and color_name
#Gradient_name = "detailed" or "smooth" or "blocks"
#color_name = "white" or "green" or "red" or "cyan" or "yellow"

gradient_name = "detailed"
color_name = "green"

contrast = 1.5
brightness = 0
gamma = 0.8
invert = False
width = 120


def apply_gamma(gray, gamma):
    normalized = gray / 255.0
    corrected = normalized ** gamma
    return (corrected * 255).astype("uint8")


def to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.convertScaleAbs(gray, alpha=contrast, beta=brightness)
    gray = apply_gamma(gray, gamma)

    if invert:
        gray = 255 - gray

    height, original_width = gray.shape
    aspect_ratio = height / original_width
    new_height = int(width * aspect_ratio * 0.45)

    resized = cv2.resize(gray, (width, new_height))

    chars = ASCII_GRADIENTS[gradient_name]
    color = COLOR_MODES[color_name]

    ascii_image = ""

    for row in resized:
        for pixel in row:
            index = int(pixel / 255 * (len(chars) - 1))
            ascii_image += color + chars[index]
        ascii_image += "\n"

    return ascii_image + Style.RESET_ALL


capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Could not open webcam")
    exit()


try:
    while True:
        ret, frame = capture.read()

        if not ret:
            break

        ascii_frame = to_ascii(frame)
        

        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_frame)

        time.sleep(0.03)

except KeyboardInterrupt:
    print("Stopped...")

finally:
    capture.release()
    cv2.destroyAllWindows()