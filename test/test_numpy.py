from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
import numpy.testing as nt
# added
import numpy as np
from PIL import Image
from instapy.io import display


def test_color2gray(image, reference_gray):

    grayscale_im = numpy_color2gray(image)
    #display(grayscale_image)

    #test unit
    assert grayscale_im.shape == (image.shape[0], image.shape[1], image.shape[2])
    assert grayscale_im.shape == reference_gray.shape
    assert grayscale_im.dtype == np.uint8
    
    height = 50
    width = 125 
    test_arr = np.empty_like(image)
    pixel = image[height, width]
    c = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]
    test_arr[height, width] = [c, c, c]

    np.testing.assert_allclose(grayscale_im[height, width], test_arr[height][width])
    #testing for channel with reference_gray
    np.testing.assert_allclose(grayscale_im[height, width], reference_gray[height, width])


def test_color2sepia(image, reference_sepia):
    sepia_im = numpy_color2sepia(image)
    #test unit
    assert sepia_im.shape == (image.shape[0], image.shape[1], image.shape[2])
    assert sepia_im.shape == reference_sepia.shape
    assert sepia_im.dtype == np.uint8
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    height = 25
    width = 50
    pixel = image[height][width]
    
    #test whether all rgb values on that particular pixle giving the roughly the same value
    red = min(255, sepia_matrix[0][0] * pixel[0] + sepia_matrix[0][1] * pixel[1] + sepia_matrix[0][2] * pixel[2])
    green = min(255, sepia_matrix[1][0] * pixel[0] + sepia_matrix[1][1] * pixel[1] + sepia_matrix[1][2] * pixel[2])
    blue = min(255, sepia_matrix[2][0] * pixel[0] + sepia_matrix[2][1] * pixel[1] + sepia_matrix[2][2] * pixel[2])
    test_arr = np.empty_like(image)
    test_arr[height, width] = [red, green, blue]
    np.testing.assert_allclose(sepia_im[height, width], test_arr[height, width])

    np.testing.assert_allclose(sepia_im[height, width], reference_sepia[height, width])

