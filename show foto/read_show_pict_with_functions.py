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
# this function show an image.it takes one parameter,image2show.
def show_image(image2show): # def defines a function named:show image.it takes one parameter:image2show
	cv.imshow("andrea", image2show) # show the image hold by the image2show variable.
	cv.waitKey(0)                   # (0) waits 4 ever. click any key to continue.
	                                # this function returns no value.
###############################################

while True:	# this is a loop that flows between lines 24 to 36, until the value of count variable ,defined
	# at line 4, reaches a value equal to 3.
	
	returned_imagen=read_image(Image_dir_+"andrea"+str(count)+".png") # it calls or execute read_image, an already defined function. 
	# It passes a value to read_image function.this value is the path to the directory where the picture to show is located.
	# That directory is hold by Image_dir_ variable, already defined at line:5
	# read_image function, returns a value:read_imagen.that variable assigned at line 10, holds the actual picture.
	# that returned value at line 12 (picture), is assigned to returned_imagen variable at line 25.
	show_image(returned_imagen)# this line execute show_image, an already defined funtion at line 18.
	# it passes the picture hold by returned_imagen variable, to show_image function.
	# show_image function, returns no value.theres no return line, at the end of that function.	  
	count=count+1 # adds one, to the value of count variable. its a counter by one .
	if(count==4): # when counts variable reaches 4, the continous loop is broken. and the flow of the script,
		break	  # jumps to line 37, and then goes on to line 39.

cv.destroyAllWindows()     # destroy all open windows.
print("Listo el pollo!")   # chicken ready!

##########################################################################################

# with this script, we can read and show four different images, defining only one function that read
# the images: read_image() . and defining another only one that shows the images: show_image() function.
# to read we need to pass the path of those pictures, to read_image function.
# at line 25 we can see that the image hold by returned_imagen, depends on the value of variable count, that
# increment by one, with each while True:loop 
# (Image_dir_+"andrea"+str(count)+".png") would be equal to:"C:\\Users\libro\Downloads/andrea0.png" for count=0.
# (Image_dir_+"andrea"+str(count)+".png") would be equal to:"C:\\Users\libro\Downloads/andrea1.png" for count=1 etc.
# for count=3, for instance str(count) is equal to:string(3) or text 3.
# in this way we can read four images using the value of count variable, as an index.
##########################################################################################

