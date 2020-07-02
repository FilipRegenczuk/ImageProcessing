import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./images/rtg_palm.jpg', cv2.IMREAD_GRAYSCALE)



print(img)

img =  * img
print(img)
plt.imshow(img, cmap="gray"), plt.axis("off")
plt.title("Orginal")

# plt.figure()
# plt.imshow(img_canny, cmap="gray"), plt.axis("off")
# plt.title("Edges")

# plt.figure()
# plt.imshow(img_binarized, cmap="gray"), plt.axis("off")
# plt.title("Binarized")

# plt.figure()
# plt.imshow(img_gaussian_blur, cmap="gray"), plt.axis("off")

plt.show()