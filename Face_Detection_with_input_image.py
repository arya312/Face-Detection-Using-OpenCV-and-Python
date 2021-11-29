import cv2
import sys

# Get user supplied values
print("The path followed by the file is: ", sys.argv[0])
Path = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + Path)
            
# Read the image
original_image = cv2.imread("D://faces.jpg",)

# Change the image into grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("{0} faces detected".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(original_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Image", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
