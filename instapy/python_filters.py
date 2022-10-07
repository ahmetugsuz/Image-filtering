"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    # iterate through the pixels, and apply the grayscale transform
    pixels = image.copy()
    grayscale_im = np.empty_like(image)
    red = 0
    green = 0
    blue = 0
    c = 0
    for height in range(pixels.shape[0]):
        for width in range(pixels.shape[1]):
            pixel = pixels[height][width]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            c = (0.21 * red) + (0.72 * green) + \
                (0.07 * blue)  # formula for gray
            grayscale_im[height][width] = [c, c, c]

    grayscale_im = grayscale_im.astype("uint8")

    return grayscale_im


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    pixels = image.copy()
    sepia_image = np.empty_like(image)


    # Iterate through the pixels
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    red = 0
    green = 0
    blue = 0

    for height in range(pixels.shape[0]):
        for width in range(pixels.shape[1]):
            pixel = image[height][width]

            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            M_red = min(255, (sepia_matrix[0][0] * red) + (sepia_matrix[0][1] * green) + (sepia_matrix[0][2] * blue))
            M_green = min(255, (sepia_matrix[1][0] * red) + (sepia_matrix[1][1] * green) + (sepia_matrix[1][2] * blue))
            M_blue = min(255, (sepia_matrix[2][0] * red) + (sepia_matrix[2][1] * green) + (sepia_matrix[2][2] * blue))

            sepia_image[height, width] = [M_red, M_green, M_blue]

    # confirm pixel range is 0-255
    #print('Data Type: %s' % sepia_image.dtype)
    #print('Min: %.3f, Max: %.3f' % (sepia_image.min(), sepia_image.max()))
    
    assert sepia_image.min() >= 0 and sepia_image.max() <= 255

    # Return image
    # don't forget to make sure it's the right type!
    sepia_image = sepia_image.astype("uint8")
    return sepia_image
