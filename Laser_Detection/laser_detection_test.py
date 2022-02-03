import cv2
import numpy as np
import laser_detect as detect
import sys

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
    
    # Run Detection
    detect_flag = detect.detect_red_laser_beam(frame, rgb_thres=100)
    
    # Add Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50,50)
    fontScale = 1
    color = (255, 0, 255)
    thickness = 2
    if (detect_flag == True):
        new_frame = cv2.putText(frame, 'Laser Detected', org, font, \
                   fontScale, color, thickness, cv2.LINE_AA)
    else:
        new_frame = cv2.putText(frame, 'No Detection', org, font, \
                   fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow(win_name, new_frame)


source.release()
cv2.destroyWindow(win_name)

