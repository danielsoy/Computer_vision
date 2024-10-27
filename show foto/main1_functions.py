import cv2 as cv  # import opencv2 as cv.you need to install it before to import it.

count = 0  # count variable is defined and loaded with value zero.
Image_dir_  = "C:\\Users\libro\Downloads/" ## path to the folder with pictures to read and show.

###############################################
# this function reads an image from a directory. we need to define a function, before we can use it.
def read_image(imagen_path):	# def defines the function named:read_image. it takes one parameter:imagen_path
	read_imagen = cv.imread(imagen_path) # read the image located at the directory pointed by imagen_path variable.
										 # assign the read image, to read_image variable.	
	return read_imagen # returns the read image.
###############################################

###############################################
# this function shows an image.it takes one parameter,image2show.
def show_image(image2show): # def defines a function named:show image.it takes one parameter:image2show
	cv.imshow("andrea", image2show) # show the image hold by the image2show variable.
	cv.waitKey(0)                   # (0) waits 4 ever. click any key to continue.
	                                # this function returns no value.
###############################################