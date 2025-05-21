# OPENING--AND-CLOSING
### Aim
To implement Opening and Closing using Python and OpenCV.

### Software Required
1. Anaconda - Python 3.7
2. OpenCV
   
### Algorithm:
#### Step1:
Create a white image of specified size and add black text ("Sam") to it using cv2.putText.
#### Step2:
Add random salt-and-pepper noise to the image by setting random pixels to black or white.
#### Step3:
Create a smaller structuring element (kernel) of size 5x5 using np.ones().
### Step4:
Apply the Opening operation using cv2.morphologyEx() with erosion followed by dilation.
### Step5:
Apply the Closing operation using cv2.morphologyEx() with dilation followed by erosion.

## Program:
```
NAME:VARSHINI D
REF NO:212223230234

## Import the necessary packages

import cv2
import numpy as np
from matplotlib import pyplot as plt

## Create the Text using cv2.putText

img = np.ones((300, 600), dtype="uint8") * 255  # Create a white image
cv2.putText(img, 'VARSHINI', (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)  # Add black text 'Sam'
noise = np.random.rand(*img.shape)
img[noise < 0.05] = 0  # Random black pixels (salt)
img[noise > 0.95] = 255  # Random white pixels (pepper)
kernel = np.ones((5, 5), np.uint8)  # A smaller 5x5 square kernel
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.figure(figsize=(12, 8))

## Original image with noise

plt.subplot(1, 3, 1)
plt.title('Original Image with Noise')
plt.imshow(img, cmap='gray')
plt.axis('off')

## Opening image

plt.subplot(1, 3, 2)
plt.title('Opening Operation')
plt.imshow(opening, cmap='gray')
plt.axis('off')

## Closing image

plt.subplot(1, 3, 3)
plt.title('Closing Operation')
plt.imshow(closing, cmap='gray')
plt.axis('off')

plt.show()
```
## Output:
### Display the input Image
![5](https://github.com/user-attachments/assets/57a98d7d-f471-4b07-9df5-0292addea4b8)


### Display the result of Opening
![6](https://github.com/user-attachments/assets/167931f0-05b1-4ef0-9ed5-3b09663121c1)


### Display the result of Closing
![7](https://github.com/user-attachments/assets/35dc6a51-dc04-4829-b2d2-8b28afd1343c)



## Result
Thus the Opening and Closing operation is used in the image using python and OpenCV.
