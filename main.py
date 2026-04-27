import cv2
import os
import time

ASCII_Char = " .:-=+*#%@"

def to_ascii(frame, width=100):
     gray  =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     height, original_width = gray.shape
     aspect_ratio = height / original_width
     new_height = int(width * aspect_ratio * 0.45)

     resized = cv2.resize(gray,(width, new_height))

     ascii_image = ""
     for row in resized:
          for pixel in row:
               pixel = 255 - pixel
               index = int(pixel / 255 * (len(ASCII_Char) - 1))
               ascii_image += ASCII_Char[index]
          ascii_image += "\n"
     return ascii_image

capture = cv2.VideoCapture(0)

if not capture.isOpened():
     print("Could not open webcam")
     exit()
try:
     while True:
          ret, frame = capture.read()

          if not ret:
               break
          ascii_frame = to_ascii(frame, width=120)

          os.system("cls" if os.name == "nt" else "clear")
          print(ascii_frame)

          time.sleep(0.03)

except KeyboardInterrupt:
     print("Stopped...")
finally:
     capture.release()