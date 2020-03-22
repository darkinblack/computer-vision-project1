import cv2
import numpy as np
import sys


# read arguments
if(len(sys.argv) != 7) :
    print(sys.argv[0], ": takes 6 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: w1 h1 w2 h2 ImageIn ImageOut.")
    print("Example:", sys.argv[0], " 0.2 0.1 0.8 0.5 fruits.jpg out.png")
    sys.exit()

w1 = float(sys.argv[1])
h1 = float(sys.argv[2])
w2 = float(sys.argv[3])
h2 = float(sys.argv[4])
name_input = sys.argv[5]
name_output = sys.argv[6]


# w1 = 0
# h1 = 0
# w2 = 1
# h2 = 0.5
# name_input = "test1.jpg"
# name_output = "out.png"

# check the correctness of the input parameters
if(w1<0 or h1<0 or w2<=w1 or h2<=h1 or w2>1 or h2>1) :
    print(" arguments must satisfy 0 <= w1 < w2 <= 1, 0 <= h1 < h2 <= 1")
    sys.exit()

# read image
inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)
if(inputImage is None) :
    print(sys.argv[0], ": Failed to read image from: ", name_input)
    sys.exit()
# cv2.imshow("input image: " + name_input, inputImage)

luvimage = cv2.cvtColor(inputImage,cv2.COLOR_BGR2Luv)
labimage = cv2.cvtColor(inputImage,cv2.COLOR_BGR2Lab)
xyzimage = cv2.cvtColor(inputImage,cv2.COLOR_BGR2XYZ)

# check for color image and change w1, w2, h1, h2 to pixel locations 
rows, cols, bands = inputImage.shape
if(bands != 3) :
    print("Input image is not a standard color image:", inputImage)
    sys.exit()

W1 = round(w1*(cols-1))
H1 = round(h1*(rows-1))
W2 = round(w2*(cols-1))
H2 = round(h2*(rows-1))
#lscl
Llist = []
tmp3 = np.copy(luvimage)

#compute b-a
for i in range(H1, H2+1) :
    for j in range(W1, W2+1) :
        Llist.append(tmp3[i,j,0])
b_a = max(Llist)-min(Llist)
minlist = min(Llist)

newimage = []
for i in Llist:
    newimage.append(int((i-minlist)*(255/b_a)))

k = 0
for i in range(H1, H2+1) :
    for j in range(W1, W2+1) :
        tmp3[i,j,0] = newimage[k]
        k+=1

labed = cv2.cvtColor(tmp3,cv2.COLOR_Luv2BGR)

cv2.imwrite(name_output,labed)


