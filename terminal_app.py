import cv2
import sys
import numpy as np

from matplotlib import pyplot as plt
from skimage import exposure


def interface():

    image_file = None

    while True:
        print("\n----------------------------")
        print("IMAGE READER")
        print("----------------------------")
        print("Loaded file:", image_file)
        print("\nChoose option:")
        print("1. Enter an image")
        print("2. Print orginal image")
        print("3. Point transformation of image")
        print("4. Gamma correction of image")
        print("5. Gaussian blur of image")
        print("5. Quit\n")

        while True:
            try:
                choice = int(input("=> "))
                break
            except ValueError:
                print("Valid option!")


        while True:

            if choice == 1:

                image_file = input("Enter image name: ")

                if image_file.endswith(".jpg") or image_file.endswith(".png"):
                    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
                    
                else:
                    print("File must be .jpg or .png type!")
                
                break
            
            if choice == 2:

                if image_file == None:
                    print("Enter an image first!")
                
                else:
                    plt.imshow(img, cmap="gray"), plt.axis("off")
                    plt.title("Orginal")
                    plt.show()
                
                break

            if choice == 3:

                if image_file == None:
                    print("Enter an image first!")

                else:
                    # Print non edited image
                    plt.subplot(121)
                    plt.imshow(img, cmap="gray"), plt.axis("off")
                    plt.title("Orginal")

                    # Multiply img per const
                    print("Enter constant: ")
                    c = int(input())
                    img_edited = c * img

                    # Print edited image
                    plt.subplot(122)
                    plt.imshow(img_edited, cmap="gray"), plt.axis("off")
                    plt.title("Image multiplied by c=" + str(c))
                    plt.show()

                break

            if choice == 4:

                if image_file == None:
                    print("Enter an image first!")

                else:
                    # Print non edited image
                    plt.subplot(121)
                    plt.imshow(img, cmap="gray"), plt.axis("off")
                    plt.title("Orginal")

                    # Print edited image
                    print("Enter constant: ")
                    c = float(input())
                    gamma_corrected = exposure.adjust_gamma(img, c)

                    plt.subplot(122)
                    plt.imshow(gamma_corrected, cmap="gray"), plt.axis("off")
                    plt.title("Gamma corrected")
                    plt.show()

                break

            if choice == 5:
                
                if image_file == None:
                    print("Enter an image first!")

                else:
                    # Print non edited image
                    plt.subplot(121)
                    plt.imshow(img, cmap="gray"), plt.axis("off")
                    plt.title("Orginal")

                    # Print edited image
                    print("Enter mask size (R x R): ")
                    r = int(input("R = "))
                    ksize = (r,r)
                    gaussian_blur = cv2.GaussianBlur(img, ksize, 0)

                    plt.subplot(122)
                    plt.imshow(gaussian_blur, cmap="gray"), plt.axis("off")
                    plt.title("Gaussian blur - mask " + str(r) + " x " + str(r))
                    plt.show()

                break


            if choice == 10:
                sys.exit()



interface()