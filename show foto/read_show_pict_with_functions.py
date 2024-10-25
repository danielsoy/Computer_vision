import cv2 as cv  # import opencv2 as cv.you need to install it before to import it.

##########################################################################################

Image_dir = "C:\\Users\libro\Downloads/andrea.jpg" ## path to the picture to read and show.

################################################
# this function reads an image from a directory. we need to define a function, before we can use it.
def read_image(imagen_path):	# def defines the function named:read_image. it takes one parameter:imagen_path
	read_imagen = cv.imread(imagen_path) # read the image located at the directory pointed by imagen_path variable.
										 # assign the read image, to read_image variable.	
	return read_imagen # returns the read image.
################################################


###############################################
# this function show an image.it takes one parameter,image2show.
def show_image(image2show): # def defines a function named:show image.it takes one parameter:image2show
	cv.imshow("andrea", image2show) # show the image hold by the image2show variable.
	cv.waitKey(0)                   # (0) waits 4 ever. click any key to continue.
###############################################


returned_imagen=read_image(Image_dir) # it calls or execute read_image, an already defined function is located..
# It passes a value to read_image function.this value is the path to the directory where the picture to show
# That directory is hold by Image_dir variable, already defined at line:5
# read_image function, returns a value:read_imagen.that variable holds the actual picture, assigned at line:10.
# that returned value at line 12 (picture), is assigned to returned_imagen variable at line 25.

show_image(returned_imagen)# this line execute show_image, an already defined funtion at line 18.
# it passes the picture hold by returned_imagen variable, to show_image function.
# show_image function, returns no value.



cv.destroyAllWindows()     # destroy all open windows.
print("Listo el pollo!")   # chicken ready!

