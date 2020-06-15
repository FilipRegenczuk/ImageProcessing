import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./images/rtg_chest.jpg', cv2.IMREAD_GRAYSCALE)

# Wykrycie krawedzi
# median_intensity = np.median(img)
# lower_threshold = int(max(0, (1.0 - 0.4) * median_intensity))
# upper_threshold = int(min(255, (1.0 + 0.4) * median_intensity))
# img_canny = cv2.Canny(img, lower_threshold, upper_threshold)


# Binaryzowanie obrazu
# max_output_value = 255
# neighborhood_size = 99
# subtract_from_mean = 10
# img_binarized = cv2.adaptiveThreshold(img, max_output_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, neighborhood_size, subtract_from_mean)


# Rozmycie Gaussowskie
img_gaussian_blur = cv2.GaussianBlur(img, (25, 25), 0)


plt.imshow(img, cmap="gray"), plt.axis("off")
plt.title("Orginal")

# plt.figure()
# plt.imshow(img_canny, cmap="gray"), plt.axis("off")
# plt.title("Edges")

# plt.figure()
# plt.imshow(img_binarized, cmap="gray"), plt.axis("off")
# plt.title("Binarized")

plt.figure()
plt.imshow(img_gaussian_blur, cmap="gray"), plt.axis("off")

plt.show()