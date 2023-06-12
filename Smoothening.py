import cv2
# absolute path of the input image file
path = "./task2/pillar.png"
# reading image 
image = cv2.imread(path)
median = image.copy()
gaussian = image.copy()
median = cv2.medianBlur(median,7)
gaussian = cv2.GaussianBlur(gaussian, (7, 7), cv2.BORDER_DEFAULT)
# Display image in a window
cv2.imshow("Original",image)
cv2.imshow("Median Blur",median)
cv2.imshow("Gaussian Blur",gaussian)
cv2.waitKey()  # Wait until any key press (press any key to close the window)
cv2.destroyAllWindows()  # kill all the windows