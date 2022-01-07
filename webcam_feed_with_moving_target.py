import cv2
import sys
import numpy as np
# import matplotlib as plt
# from PIL import Image

# Find and Select Camera
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

# Set up video capture object
source = cv2.VideoCapture(s)

# Set up video camera window
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Get Size of Frame, Re-Size Window
has_frame, frame = source.read()
height, width, _ = np.shape(frame)
cv2.resizeWindow(win_name, width, height)

# Initialize Target Coordinates
has_frame, frame = source.read()
h, v, d = np.shape(frame)
target = [int(height/2), int(width/2)]


# while loop while video is being captured
while cv2.waitKey(1) != 27: # Escape

    # Get Frame from Camera
    has_frame, frame = source.read()
    if not has_frame:
        break
    
    # flip the image for normal view
    frame = cv2.flip(frame, 1)
    
    # Make Copy of Frame
    overlay = frame.copy()
    
    # Logic for moving target
    step = 10; # pixels
    # Move Target Up
    if cv2.waitKey(1) == ord('w'):
        if target[1] >= 0 + (2*step):
            target[1] = target[1] - step;
    # Move Target Down        
    elif cv2.waitKey(1) == ord('s'):
        if target[1] <= (height - (2*step)):
            target[1] = target[1] + step;
    # Move Target Right        
    elif cv2.waitKey(1) == ord('a'):
        if target[0] >= (0 + (2*step)):
            target[0] = target[0] - step;
    # Move Target Left        
    elif cv2.waitKey(1) == ord('d'):
        if target[0] <= (width - (2*step)):
            target[0] = target[0] + step;
    
    # add rectangle target to image
    size = 20;
    cv2.rectangle(overlay, \
                 (target[0] - size, target[1] - size), \
                 (target[0] + size, target[1] + size), \
                 (255, 0, 255), \
                  2)
    
    # show the final image without target
    alpha = 0.35;
    new_frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    cv2.imshow(win_name, new_frame)


source.release()
cv2.destroyWindow(win_name)