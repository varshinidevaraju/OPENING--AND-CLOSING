#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[3]:


img = np.ones((300, 600), dtype="uint8") * 255  
cv2.putText(img, 'VARSHINI', (160, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)  
noise = np.random.rand(*img.shape)
img[noise < 0.05] = 0  
img[noise > 0.95] = 255  
kernel = np.ones((5, 5), np.uint8)  
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.figure(figsize=(12, 8))


# In[4]:


plt.subplot(2, 3, 2)
plt.title('Original Image with Noise')
plt.imshow(img, cmap='gray')
plt.axis('off')


# In[5]:


plt.subplot(1, 3, 2)
plt.title('Opening Operation')
plt.imshow(opening, cmap='gray')
plt.axis('off')


# In[6]:


plt.subplot(1, 3, 3)
plt.title('Closing Operation')
plt.imshow(closing, cmap='gray')
plt.axis('off')
plt.show()


# In[ ]:


`

