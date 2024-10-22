import cv2
import numpy as np # please add numpy libraries and rename it

cap = cv2.VideoCapture(0)   # get input resources (0 = origin source (internal webcam))

while True:
    ret, frame = cap.read()
    # print(frame.shape) # print out the captured size of frame
    resized = cv2.resize(frame, (960,540)) # resize desired viewable output size

    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    low_color = np.array([2, 110, 171 ])          #min range of colour
    high_color = np.array ([35, 255, 255])         #max range of colour
    color_mask = cv2.inRange(hsv, low_color, high_color)    #masking between two range of colour
    # color = cv2.bitwise_and(resized, resized, mask=color_mask)

    blur = cv2.GaussianBlur(color_mask, (15, 15), 0)

    cv2.imshow("Masked Color", color_mask) # white = True, black = False
    cv2.imshow("Blur", blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()