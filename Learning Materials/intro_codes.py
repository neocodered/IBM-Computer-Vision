from PIL import Image
import matplotlib.pyplot as plt
import cv2

# # image = Image.open("Baboon.png")
# # plt.imshow(image)
# # image.show()

image = cv2.imread("Baboon.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blue, green, red = image_rgb[:,:,0], image_rgb[:,:,1], image_rgb[:,:,2]

# plt.imshow(blue)
# plt.title("Blue")
plt.imshow(green)
plt.title("Green")
# plt.imshow(red)
# plt.title("Red")

plt.show()


# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create the plot
# plt.plot(x, y)

# # Add a title and labels
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")

# # Show the plot
# plt.show()
