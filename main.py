import cv2


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ret = True

while ret:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        exit()
    elif key == 32:
        pause = True
        while pause:
            key = cv2.waitKey(1)
            if key == 32:
                pause = False
            elif key == 27:
                exit()