
import sys
import time
import cv2 as cv
import numpy as np 
from PIL import ImageGrab


for i in range (0, 6):
	time.sleep(5)


screen = np.array(ImageGrab.grab(bbox(0, 40, 800, 640)))
print(sys.version)
