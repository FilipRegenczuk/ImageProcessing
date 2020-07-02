import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure


img = cv2.imread('./images/rtg_palm.jpg', cv2.IMREAD_GRAYSCALE)
img = exposure.adjust_gamma(img, 10)
equalized = cv2.equalizeHist(img)

plt.subplot(221)
plt.imshow(img, cmap="gray"), plt.axis("off")
plt.title("Orginal")

plt.subplot(222)
plt.hist(img.ravel(), 256, [0,256])
plt.title("Orginal - histogram")

plt.subplot(223)
plt.imshow(equalized, cmap="gray"), plt.axis("off")
plt.title("Equalized")

plt.subplot(224)
plt.hist(equalized.ravel(), 256, [0,256])
plt.title("Equalized - histogram")






# plt.figure()
# plt.subplot(122)
# gamma_corrected = exposure.adjust_gamma(img, 2)
# plt.imshow(gamma_corrected, cmap="gray"), plt.axis("off")
# plt.title("Gamma corrected")

# plt.figure()
# plt.imshow(img_canny, cmap="gray"), plt.axis("off")
# plt.title("Edges")

# plt.figure()
# plt.imshow(img_binarized, cmap="gray"), plt.axis("off")
# plt.title("Binarized")

# plt.figure()
# plt.imshow(img_gaussian_blur, cmap="gray"), plt.axis("off")

plt.show()