from main1_functions import * # with * at the end, we import all the functions and variables,defined at main1_function.py
                              # now those functions and variables, are available to main1.py script or any other 
							  # python script to be used.

##################################################################################################################
							     
while True:	# this while True: loop, reads an shows images calling returned_imagen, and show_image functions.
			# using the value of count variable as an index, to point to the folder directory where the images
			# are located. when count variable reaches some x value(4 for our case), the loop is broken at line 13.
			# and the flow of the programm, can go on from line 18.

	
	returned_imagen=read_image(Image_dir_+"andrea"+str(count)+".png") # calls read_image function.saves the returned
																	  # value (image to show) at returned_imagen variable.	 
	show_image(returned_imagen) # execute show_image function.it passes the image to show tru returned_image.
	
	count=count+1 # increment count variable by one.
	if(count==4): # jumps to the next line, if count=4. if not, keeps the execution flow, within the loop.back to line 5
		break	  # get out of the loop.

cv.destroyAllWindows()     # destroy all open windows.
print("Listo el pollo!")   # chicken ready!



