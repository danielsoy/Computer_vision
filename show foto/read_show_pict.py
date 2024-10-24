
import cv2 as cv  # import opencv2 as cv.you need to install it before import it.

############################

Image = cv.imread("C:\\anodet/notebooks\show foto/andrea pietra.jpg") # path to the picture to read and show.

cv.imshow("andrea", Image)

cv.waitKey(0)             # (0) waits 4 ever. click space bar to continue.
                           
cv.destroyAllWindows()    # destroy all open windows. 

print("Listo el pollo!")