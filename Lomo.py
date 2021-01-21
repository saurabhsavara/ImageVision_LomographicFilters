import cv2
import numpy as np
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(parser.parse_args())
img_path = args['image']
slider_s_max = 20
slider_r_max= 100
s_value=8
r_value=100
title_window = 'LUT transformation'
lookuparray = np.empty(256, dtype=np.uint8)
img = cv2.imread(img_path)
img_resize = cv2.resize(img, (500, 500))
rows, cols = img_resize.shape[:2]
cv2.imshow(title_window,img_resize)
output=img;

def on_s_trackbar(val):
    global s_value
    s_value=val
    if s_value<=7:
        s_value=8
        perform_transform()
    else:
        perform_transform()

def lutformula (i, s):
    i_value=np.float(i/256.0)
    return round(256*(1 / (1 +(np.power(math.e, (-(i_value - 0.5) / (s/100)))))))


def on_r_trackbar(val):
    global r_value
    r_value=val
    perform_transform()

def perform_transform():
    global output
    img_norm = img_resize.astype(np.uint8) / 255.0
    (blue, green, red) = cv2.split(img_resize)
    for i in range(256):
        lookuparray[i] = lutformula(i, s_value)
    red_new = cv2.LUT(red, lookuparray)
    img1 = cv2.merge([blue,green,red_new])
    rows, cols = img1.shape[:2]
    percent = (r_value / 100) * 255
    X_resultant_kernel = cv2.getGaussianKernel(cols, percent)
    Y_resultant_kernel = cv2.getGaussianKernel(rows, percent)
    resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = percent * resultant_kernel / np.linalg.norm(resultant_kernel)
    output = np.copy(img1)
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask
    cv2.imshow(title_window, output)





cv2.namedWindow(title_window)
trackbar_s_value = 'S value s %d' % slider_s_max
trackbar_r_value = 'R value r %d' % slider_r_max
cv2.createTrackbar(trackbar_s_value, title_window , 10, slider_s_max, on_s_trackbar)
cv2.createTrackbar(trackbar_r_value,title_window,100,slider_r_max,on_r_trackbar)

while True:
    c = cv2.waitKey()
    if c==ord('q'):
        cv2.destroyWindow(title_window)
        break;
    if c==ord('s'):
        cv2.imwrite(img_path+str(s_value/100)+"_"+str(r_value)+".png",output)
        cv2.destroyWindow(title_window)
        break;


def main():
    print("Program has been terminated")

if __name__ == "__main__": main()
