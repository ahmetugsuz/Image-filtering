from instapy.python_filters import python_color2gray, python_color2sepia
#added
from instapy.io import display, read_image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from instapy import get_filter

def test_color2gray(image):
    grayscale_im = python_color2gray(image) 
    #saving the image
    gray_image = Image.fromarray(grayscale_im)
    gray_image.save("rain_grayscale.jpg")

    # check that the result has the right shape, type
    assert grayscale_im.shape == (image.shape[0], image.shape[1], image.shape[2])
    assert grayscale_im.dtype == "uint8"
    # assert uniform r,g,b values
    height = 50
    width = 150
    assert grayscale_im[height, width][0] == grayscale_im[height, width][1] == grayscale_im[height, width][2]

    
    test_arr = image.copy()
    pixel = image[height, width]
    c = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
    test_arr[height, width] = [c, c, c]

    np.testing.assert_allclose(grayscale_im[height, width], test_arr[height][width])




def test_color2sepia(image):
    # run color2sepi-a
    sepia_im = python_color2sepia(image)

    #saving the sepia image
    sepia_image = Image.fromarray(sepia_im)
    sepia_image.save('rain_sepia.jpg')

    # check that the result has the right shape, type
    assert sepia_im.shape == (image.shape[0], image.shape[1], image.shape[2])
    assert sepia_im.dtype == np.uint8

    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    test_arr = np.empty_like(image)
    height = 100
    width = 100
    pixel = image[height][width]
    #testing whether if red values are equal, or very similar
    #np.testing.assert_allclose(sepia_im[height, width][0], test_arr[height, width][0])

    #test whether all rgb values on that particular pixle giving the roughly the same value
    red = min(255, (sepia_matrix[0][0] * pixel[0]) + (sepia_matrix[0][1] * pixel[1]) + (sepia_matrix[0][2] * pixel[2]))
    green = min(255, (sepia_matrix[1][0] * pixel[0]) + (sepia_matrix[1][1] * pixel[1]) + (sepia_matrix[1][2] * pixel[2]))
    blue = min(255, (sepia_matrix[2][0] * pixel[0]) + (sepia_matrix[2][1] * pixel[1]) + (sepia_matrix[2][2] * pixel[2]))
    test_arr[height, width] = [red, green, blue]
    np.testing.assert_allclose(sepia_im[height, width], test_arr[height, width], atol=1)

