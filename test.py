import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure


img = cv2.imread('./images/rtg_palm.jpg', cv2.IMREAD_GRAYSCALE)



print(img)
img = 1 * img
print(img)
plt.imshow(img, cmap="gray"), plt.axis("off")
plt.title("Orginal")

plt.figure()
gamma_corrected = exposure.adjust_gamma(img, 2)
plt.imshow(gamma_corrected, cmap="gray"), plt.axis("off")
plt.title("Gamma corrected")

# plt.figure()
# plt.imshow(img_canny, cmap="gray"), plt.axis("off")
# plt.title("Edges")

# plt.figure()
# plt.imshow(img_binarized, cmap="gray"), plt.axis("off")
# plt.title("Binarized")

# plt.figure()
# plt.imshow(img_gaussian_blur, cmap="gray"), plt.axis("off")

plt.show()