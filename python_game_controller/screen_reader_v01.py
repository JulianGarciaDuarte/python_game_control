
import sys
import time
import cv2 
import numpy as np 
from PIL import ImageGrab



def screen_reader():
	last_time = time.time()
	while(True):

		screen = np.array(ImageGrab.grab(bbox= (0, 40, 800, 1000)))

		print('loop took {} seconds'.format(time.time()- last_time))
		last_time = time.time()

		cv2.imshow('Window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

		if cv2.waitKey(25) & 0xff == ord('q'):
			cv2.destroyAllWindows()
			break

for i in range (0, 6):
	time.sleep(1)
	print(i)
screen_reader()
print(sys.version)
