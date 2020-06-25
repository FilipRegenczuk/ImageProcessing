import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

def interface():

    image_file = None

    while True:
        print("\n----------------------------")
        print("IMAGE READER")
        print("----------------------------")
        print("Loaded file:", image_file)
        print("\nChoose option:")
        print("1. Enter an image")
        print("2. Print an image")
        print("3. Quit\n")

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
                    print("Enter image first!")
                    break
                
                else:
                    plt.imshow(img, cmap="gray"), plt.axis("off")
                    plt.title("Orginal")
                    plt.show()
                
                break

            if choice == 3:
                sys.exit()


interface()