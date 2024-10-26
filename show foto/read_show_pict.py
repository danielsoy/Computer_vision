import cv2 as cv  # import opencv2 as cv.you need to install it before to import it.

###################

Image = cv.imread("C:\\Users\libro\Downloads/andrea0.png") # path to the picture to read and show.

cv.imshow("andrea", Image) # chose a name for the window that will hold the image, and show it.

cv.waitKey(0)              # (0) waits 4 ever. click any key to continue.
                           
cv.destroyAllWindows()     # destroy all open windows. 

print("Listo el pollo!")   # chicken ready!

