import numpy as np
from matplotlib import pyplot as plt, cm

random_img = np.random.rand(500, 1500)
plt.imshow(random_img, cmap=cm.gray, interpolation="nearest")
plt.show()
