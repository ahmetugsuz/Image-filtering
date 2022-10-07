"""numpy implementation of image filters"""
from typing import Optional
#added
import numpy as np

def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    #pixels = np.zeros(image.shape)
    #gray_image = np.empty_like(image)
    red = np.array(image[:,:,0])
    green = np.array(image[:,:,1])
    blue = np.array(image[:,:,2])
    
    red = red * 0.21
    green = green *0.72
    blue = blue * 0.07
    pixels = image.copy()
    #pixels[:pixels.shape[0], :pixels.shape[1],] = avg

    for i in range(3):
        pixels[:,:,i] = (red + green + blue)

    # Return image (make sure it's the right type!)
    pixels = pixels.astype("uint8")

    return pixels


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")
    sepia_image = np.empty_like(image)
    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    a = 1 - 0.393
    b = 1- 0.686
    c = 1 - 0.131
    d_a = a * (1 - k)
    d_b = b * (1 - k)
    d_c = c * (1 - k)
    sepia_matrix = [
        [ 0.393 + d_a, 0.769*k, 0.189*k], 
        [ 0.349*k, 0.686 + d_b, 0.168*k],
        [ 0.272*k, 0.534*k, 0.131 + d_c],
    ]
    sepia_image = np.clip(np.einsum('ijk,lk->ijl', image, sepia_matrix), 0, 255) 

    sepia_image = sepia_image.astype("uint8")
    return sepia_image
