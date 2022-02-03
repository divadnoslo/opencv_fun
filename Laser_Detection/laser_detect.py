import cv2
import numpy as np

# Define Red Detect Funcion
def detect_red_laser_beam(image_bgr, rgb_thres=175, n_max=150):
    
    # Convert Frame from BGR to RGB
    image_rgb = image_bgr[:,:,::-1]
    
    # Build RGB Mask
    r_mask = (image_rgb[:,:,0] > rgb_thres)
    g_mask = (image_rgb[:,:,1] > rgb_thres)
    b_mask = (image_rgb[:,:,2] > rgb_thres)
    rgb_mask = r_mask & g_mask & b_mask
    
    # Build HSV Mask
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    lower_red = np.array([160, 0, 0])
    upper_red = np.array([180, 255, 255])
    hsv_mask = cv2.inRange(image_hsv, lower_red, upper_red) > 10
    
    # Combine RGB and HSV Masks
    laser_mask = 1*(rgb_mask & hsv_mask)
    
    # Determine if Detection Occured
    n_min = 1
    if (sum(sum(laser_mask)) >= n_min) & (sum(sum(laser_mask)) <= n_max):
        DETECT_FLAG = True
    else:
        DETECT_FLAG = False
    
    # Determine Location of Detection
    
    
    # Return Results
    return DETECT_FLAG