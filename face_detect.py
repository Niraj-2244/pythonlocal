import cv2
import numpy as np 


video_cap = cv2.VideoCapture(0)
while True:
    ret , video_data = video_cap.read()
    cv2.imshow("video_live", video_data)
    # cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # if cv2.waitKey(10) == ord("a"):
        # break
    
video_cap.release()