import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/forest.jpg', cv2.IMREAD_COLOR)

plt.imshow(img), plt.axis("off")
plt.show()