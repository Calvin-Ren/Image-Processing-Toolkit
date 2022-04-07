# Image-Processing-Toolkit

The Toolkit was created during the time in Big Data and Smart Computing(BDSC) by *Calvin Ren*.



**Tools included:**

#### 1. Closing Algorithm (Implemented in OpenCV)

Used to Remove tiny broken parts in the images after Semantic segmentation.

#### 2. Color Histogram 

Create Color Histogram for images.

#### 3. RGB to HSV Color System 

Color System Conversion. HSV Color System performs better in Dominent Color Extraction. Included the data Conversion and image Conversion.

#### 4. Dominent Color Extraction with K-Means 

Use K-Means Algorithm to extract the dominent color in single image.

#### 5. Exposed Detection 

Estimate if a single image is over exposed.

#### 6. Output Mask

After the Semantic segmentation, we need to maintain the selected part in the image and remove the other parts. We use this tool to only keep the segmanted parts in the images.

#### 7. Semantic Result Output 

Export the results of the DeepLab V3+, including the proportion of each semantic part in a single image. 

#### 8. Image Cilbration (Implemented in OpenCV)

Cilbration included adjustment on brightness, Saturaion and Contrast. Added with image enhancement and edge detection.

#### 9. Color Matching 

Match the result of the Dominent Color Extraction to the CBCC-240. 

#### 10. Entropy Analysis

Calculate the Entropy of images. The Result can indicate the Bright Degree of Images. 
