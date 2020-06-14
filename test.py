import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/rtg_chest.jpg', cv2.IMREAD_GRAYSCALE)

median_intensity = np.median(img)
lower_threshold = int(max(0, (1.0 - 0.4) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.4) * median_intensity))
img_canny = cv2.Canny(img, lower_threshold, upper_threshold)



plt.figure()
plt.imshow(img, cmap='gray'), plt.axis("off")
plt.title("Orginal image")

plt.figure()
plt.imshow(img_canny, cmap='gray'), plt.axis("off")
plt.title("Edges")


plt.show()