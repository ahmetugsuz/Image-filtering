"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from . import io, get_filter
from typing import Callable
import numpy as np
from instapy.numba_filters import numba_color2gray, numba_color2sepia

def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # run the filter function `calls` times
    filter_function(numba_color2gray(arguments[0])) #kaller paa funkjsonenne for at den skal leses en gang forst
    filter_function(numba_color2sepia(arguments[0]))
    avg = 0
    for i in range(calls):
        tic = time.time()
        filter_function(arguments[0])
        tac = time.time()
        avg += (tac - tic)

    avg = avg / calls
    # return the _average_ time of one call
    return avg


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    # load the image
    image = io.read_image(filename)
    # print the image name, width, height
    # iterate through the filters
    filter_names = ['color2gray', 'color2sepia']
    text_file = open("timing-report.txt", "w")
    print("Timing performed using", filename[5:9],":",str(image.shape[1])+"x"+str(image.shape[0]), file=text_file)
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = get_filter(filter_name, "python")  
        # time the reference implementation
        reference_time = time_one(reference_filter, image)
        print(
            f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})", file=text_file #skriver til tekstfilen
        )
        print(
            f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})" #print paa terminal
        )
        
        # iterate through the implementations
        implementations = ['numpy', 'numba']
        for implementation in implementations:
            filter = get_filter(filter_name, implementation)  
            # time the filter

            filter_time = time_one(filter, image)
            # compare the reference time to the optimized time
            speedup = reference_time / filter_time
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)", file=text_file #skriver til tekstfilen
            )
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)" #print paa terminal
            )
          

if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
    
