"""numba-optimized filters"""
from numba import jit
import numpy as np

@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    # iterate through the pixels, and apply the grayscale transform
    grayscale_im = np.empty_like(image)
    c = 0
    for height in range(image.shape[0]):                        
        for width in range(image.shape[1]):
            grayscale_im[height, width][0] = (0.21 * image[height][width][0]) + (0.72 * image[height][width][1]) + (0.07 * image[height][width][2])
            grayscale_im[height, width][1] = (0.21 * image[height][width][0]) + (0.72 * image[height][width][1]) + (0.07 * image[height][width][2])
            grayscale_im[height, width][2] = (0.21 * image[height][width][0]) + (0.72 * image[height][width][1]) + (0.07 * image[height][width][2])
    grayscale_im = grayscale_im.astype("uint8")
    return grayscale_im


@jit(nopython=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131],
    ]
    for height in range(image.shape[0]):
        for width in range(image.shape[1]):
            sepia_image[height, width][0] = min(255, sepia_matrix[0][0] * image[height][width][0] + sepia_matrix[0][1] * image[height][width][1] + sepia_matrix[0][2] * image[height][width][2])
            sepia_image[height, width][1] = min(255, sepia_matrix[1][0] * image[height][width][0] + sepia_matrix[1][1] * image[height][width][1] + sepia_matrix[1][2] * image[height][width][2])
            sepia_image[height, width][2] = min(255, sepia_matrix[2][0] * image[height][width][0] + sepia_matrix[2][1] * image[height][width][1] + sepia_matrix[2][2] * image[height][width][2])
    # Return image
    # don't forget to make sure it's the right type!
    sepia_image = sepia_image.astype("uint8")
    return sepia_image



