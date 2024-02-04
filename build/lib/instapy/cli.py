"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from instapy import timing 
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
    runtime: str = None,
    effect: float = 1
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    
    if scale != 1:
        # Resize image, if needed
        new_width = int((float(image.size[0]) // float(scale)))
        new_height = int((float(image.size[1]) // float(scale)))
        image = image.resize((new_width, new_height), Image.BILINEAR)

    pixels = np.asarray(image)
    # Apply the filter
    filter_function = instapy.get_filter(filter, implementation)
    if effect != 1 and implementation == "numpy" and filter == "color2sepia":
        filtered = filter_function(pixels, effect)
    else:
        filtered = filter_function(pixels)

    if runtime != None:
        time = timing.time_one(filter_function, pixels)
        print(f"Average time over 3 runs: {time}s")

    


    if out_file:
        # save the file
        im = Image.fromarray(filtered)
        im.save(out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]


    # filename is positional and required
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Input file name')
    #filterparser = parser.add_mutually_exclusive_group()
    parser.add_argument("-o", "--out", help="The output filename", nargs='?', const=0)
    parser.add_argument("-g", "--gray", help="Select gray filter", nargs='?', const=0, default='color2sepia')
    parser.add_argument("-se", "--sepia", help="Select sepia filter", nargs='?', const=0, default='color2gray')
    parser.add_argument("-sc", "--scale", help="Scale factor to resize image", nargs='?', const=1, type=float, default=1)
    parser.add_argument("-i {python,numba,numpy,cython}", "--implementation", help="The implementation",  nargs='?', const=1, default='python')
    parser.add_argument("-r", "--runtime", help="Track the runtime of the execution", nargs='?', const=0)
    parser.add_argument("-e", "--effect", help="Apply sepia effect on numpy implementation", nargs='?', type=float, const=1, default=1)
    
    
    # Add required arguments

    args = parser.parse_args()

    if len(argv) < 0:
        sys.argv.append('--help')

    # parse arguments and call run_filter
    if args.sepia:
        run_filter(args.file, args.out, args.implementation, args.sepia, args.scale, args.runtime, args.effect)
    else:    
        run_filter(args.file, args.out, args.implementation, args.gray, args.scale, args.runtime, args.effect)

    
    
    
    
