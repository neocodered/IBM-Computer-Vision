import cv2
import matplotlib.pyplot as plt

# Read the image using OpenCV
image = cv2.imread('Baboon.png')

# Split the image into its B, G, and R components
b, g, r = cv2.split(image)

# Merge the channels with zeros to create images with only one color channel
# Create an empty channel
zeros = cv2.merge((b*0, b*0, b*0))

# Red channel image
red_image = cv2.merge((zeros[:, :, 0], zeros[:, :, 1], r))

# Green channel image
green_image = cv2.merge((zeros[:, :, 0], g, zeros[:, :, 2]))

# Blue channel image
blue_image = cv2.merge((b, zeros[:, :, 1], zeros[:, :, 2]))

# Convert the images to RGB for displaying with Matplotlib
red_image_rgb = cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB)
green_image_rgb = cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB)
blue_image_rgb = cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB)

# Display the images using Matplotlib
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(red_image_rgb)
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(green_image_rgb)
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blue_image_rgb)
plt.title('Blue Channel')
plt.axis('off')

plt.show()
