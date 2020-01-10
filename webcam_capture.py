
import cv2
import time

cv2.namedWindow("preview")
vc = cv2.VideoCapture('/dev/video2')
vc.set(3, 640)
vc.set(4, 480)
vc.set(5, 30)
vc.set(cv2.CAP_PROP_BUFFERSIZE, 2)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    print(f"Acquiring video resolution: {frame.shape}")
    begin_time = time.time()
    counter = 0
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    counter += 1
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
print(f"FPS: {counter/(time.time()-begin_time)}")
cv2.destroyWindow("preview")