# ImageVision

## LomographicFilters

This program provides the user ability to apply a filter to the red color plane of an image using a look up table and also vignette filter to an image.

The Lookup Table used by the program is : 

  <a href="https://www.codecogs.com/eqnedit.php?latex=LUT_i%20=%201/(1&plus;e&space;^{-((i/256)-0.5)/s)})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?LUT_i%20=%201/(1&plus;e&space;^{-((i/256)-0.5)/s)})" title="LUT_i%20=%201/(1+e ^{-((i/256)-0.5)/s)})" /></a>

 The values of 's' will range from 0.08 to 0.20 .

 While the vignette filter will provide the user to change the filter radius (r) from 1 to 100   

# **Input**

1. Image 1 - A copy of an image which needs to be transformed.

# **Output**

1. Image 1 - The image transformed with custom s and r values.


# **Runtime Instructions**

1. Download Lomo.py to your python environment.
  1. Python version 3.7 or higher is recommended on Windows 10 or above or Mac 10 or above.
  2. Ensure you have the cv and numpy libraries installed in your python environment.
2. Download the .png images supplied or specify your own to the programs main folder.
3. Run script the program.
  1. Usinng `python Lomo.py -i *Image path/image name*` 

# **Reflection**

In order display clear visuals of increasing the darkness of dark pixels and the brightness of bright pixels we went with images of the sun and stars. This allowed us to visualize eaxctly what our Lookup Table is doing with the red color plane. The solution also allowed us to explore and handle differrent color planes with floating datatypes as well as working with the LUT forumula to calculate distinct pixel values. 
Moving onto the vignette filter, working with gradient kernels and altrering the kernel value to play around with the radius of the filter helps identify new functions in the OpenCV library that hadnt been explored before. 
