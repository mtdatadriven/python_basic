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
    color = cv2.bitwise_and(resized, resized, mask=color_mask)
    
    blur = cv2.GaussianBlur(color_mask, (15, 15), 0)    
    edge = cv2.Canny(blur, 100, 200) 

    pix = np.asarray(blur)   
    exist = np.where(pix[::]==255)
    index = np.asarray(exist[0])

    if index.size > 0:
        gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

        M = cv2.moments(thresh, binaryImage = True)
        if M["m00"] != 0:
            cX = int(M["m10"]/M["m00"])
            cY = int(M["m01"]/M["m00"])
        else:
            cX = 0
            cY = 0
        cv2.drawContours(resized, [np.array([[cX, cY]])], -1, (0, 0, 255), 2)
        cv2.circle(resized, (cX, cY), 7, (0, 255, 0), -1)

    cv2.imshow("Resized", resized)
    cv2.imshow("From edge", edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()