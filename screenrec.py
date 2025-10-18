import cv2
import numpy as np
import pyautogui

# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 60
# create the video write object
out = cv2.VideoWriter("output.mp4", fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
record_seconds = int(input("Enter the number of seconds you want to record screen. the time should be in seconds."))

for i in range(int(record_seconds * fps)):
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()

