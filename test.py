import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure


# HISTOGRAMS
# img = cv2.imread('./images/rtg_palm.jpg', cv2.IMREAD_GRAYSCALE)
# img = exposure.adjust_gamma(img, 10)
# equalized = cv2.equalizeHist(img)

# plt.subplot(221)
# plt.imshow(img, cmap="gray"), plt.axis("off")
# plt.title("Orginal")

# plt.subplot(222)
# plt.hist(img.ravel(), 256, [0,256])
# plt.title("Orginal - histogram")

# plt.subplot(223)
# plt.imshow(equalized, cmap="gray"), plt.axis("off")
# plt.title("Equalized")

# plt.subplot(224)
# plt.hist(equalized.ravel(), 256, [0,256])
# plt.title("Equalized - histogram")
######################### 


# GAUSSIAN BLUR
# img = cv2.imread('./images/cells_noise.jpg', cv2.IMREAD_GRAYSCALE)

# # Print non edited image
# plt.subplot(121)
# plt.imshow(img, cmap="gray"), plt.axis("off")
# plt.title("Orginal")

# # Print edited image
# print("Enter mask size (R x R): ")
# r = int(input("R = "))
# ksize = (r,r)
# gaussian_blur = cv2.GaussianBlur(img, ksize, 0)

# plt.subplot(122)
# plt.imshow(gaussian_blur, cmap="gray"), plt.axis("off")
# plt.title("Gaussian blur - mask " + str(r) + " x " + str(r))
# plt.show()
#########################

# MEDIAN BLUR
# img = cv2.imread('./images/cells_noise.jpg', cv2.IMREAD_GRAYSCALE)

# # Print non edited image
# plt.subplot(121)
# plt.imshow(img, cmap="gray"), plt.axis("off")
# plt.title("Orginal")

# # Print edited image
# median_blur = cv2.medianBlur(img, 5)

# plt.subplot(122)
# plt.imshow(median_blur, cmap="gray"), plt.axis("off")
# plt.title("Median blur")
# plt.show()
########################


img = cv2.imread('./images/rtg_chest.jpg', cv2.IMREAD_GRAYSCALE)

# Print non edited image
plt.subplot(131)
plt.imshow(img, cmap="gray"), plt.axis("off")
plt.title("Orginal")

# Print edited image
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
plt.subplot(132)
plt.imshow(sobelX, cmap="gray"), plt.axis("off")
plt.title("Sobel X")

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
plt.subplot(133)
plt.imshow(sobelY, cmap="gray"), plt.axis("off")
plt.title("Sobel Y")

plt.show()


laplacian = cv2.Laplacian(img, cv2.CV_64F)
plt.subplot(224)
plt.imshow(laplacian, cmap="gray"), plt.axis("off")
plt.title("Laplacian")

plt.show()



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