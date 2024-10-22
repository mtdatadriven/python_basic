import cv2

cap = cv2.VideoCapture(0)   # get input resources (0 = origin source (internal webcam))

while True:
    ret, frame = cap.read()
    # print(frame.shape) # print out the captured size of frame
    resized = cv2.resize(frame, (960,540)) # resize desired viewable output size 
    cv2.imshow("Test 1", frame)
    cv2.imshow("Test 2", resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()