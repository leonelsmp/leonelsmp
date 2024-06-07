import cv2
# Read the image
img = cv2.imread("galaxy.png")
# Print original size
print(f"Original size: {img.shape[1]}x{img.shape[0]}")
# Resize image
new_size = (1200,900)  # width, height
resized_img = cv2.resize(img, new_size)
# Save resized image
cv2.imwrite("galaxy1.jpg", resized_img)