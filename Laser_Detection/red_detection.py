import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in Image
image_bgr = cv2.imread('test3.jpg')

# Resize and Display Input Image
width = 960
height = 540
image_bgr = cv2.resize(image_bgr, (width, height)) 
image_rgb = image_bgr[:,:,::-1]
plt.imshow(image_rgb)
plt.title("Origonal Image (RGB)")

# Create RBG Mask
thres = 175
r_mask = (image_rgb[:,:,0] > thres)
g_mask = (image_rgb[:,:,1] > thres)
b_mask = (image_rgb[:,:,2] > thres)
rgb_mask = r_mask & g_mask & b_mask

plt.figure()
plt.imshow(255*rgb_mask, cmap='gray')
plt.title('RGB Mask of Laser in Image')

# Convert to HSV 
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# # Plot each HSV Channel
# h = image_hsv[:,:,0]
# s = image_hsv[:,:,1]
# v = image_hsv[:,:,2]
# plt.figure()
# plt.imshow(h, cmap='gray')
# plt.title("Hue")
# plt.figure()
# plt.imshow(s, cmap='gray')
# plt.title("Saturation")
# plt.figure()
# plt.imshow(v, cmap='gray')
# plt.title("Value")

# Define HSV Threshold for Red
lower_red = np.array([160, 0, 0])
upper_red = np.array([180, 255, 255])

# Create HSV Mask
hsv_mask = cv2.inRange(image_hsv, lower_red, upper_red)
hsv_mask = 255*((hsv_mask) > 1)

plt.figure()
plt.imshow(255*hsv_mask, cmap='gray')
plt.title('HSV Mask of Laser in Image')

# Combine Both Masks
laser_mask = rgb_mask & hsv_mask

plt.figure()
plt.imshow(255*laser_mask, cmap='gray')
plt.title('Boolean Detection of Laser in Image')