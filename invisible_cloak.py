import cv2
import numpy as np
cap = cv2.VideoCapture(0)
back = cv2.imread("image.jpg")  #reading the background image from background.py
click = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv",hsv)  

        green = np.uint8([[[0,255,0]]]) #BGR value of green
        hsv_green = cv2.cvtColor(green ,cv2.COLOR_BGR2HSV)

        # HSV value of green from BGR
        # l_green: hue-10,100,100, u_green: hue+10,255,255     
        # this is telling that the hue color ranges from lower to upper....I want to dissapear all that
        # threshold the hsv value to get only green color
        l_green = np.array([20, 80, 50])
        u_green = np.array([90, 255, 255])

        mask=cv2.inRange(hsv, l_green, u_green)

        part1 = cv2.bitwise_and(back,back,mask=mask)  #The values that were hidden by the color of cloak is replaced by what was in the background image

        mask = cv2.bitwise_not(mask)

        # Eliminating Green
        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("cloak", part1 + part2)

        if(cv2.waitKey(100) == ord('q')):
            break
        if(cv2.waitKey(100) == ord('c')):
            #Click the image
            click += 1
            cv2.imwrite("Captured" + str(click) + ".jpg", part1 + part2)

cap.release()
cv2.destroyAllWindows()