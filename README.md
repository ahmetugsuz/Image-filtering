# Image Filtering Python Package

## Overview

This package, named Instapy, allows users to apply vintage sepia or gray effects to images. The sepia effect imparts a warm brownish-grey hue, creating an aged, antique appearance. On the other hand, the gray effect converts the image to black and white. Users can adjust the intensity of the effect and scale the image according to their preferences. The program offers customizable options, providing users with control over the final result.

## Prerequisites

Ensure the following dependencies are properly installed on your system:

* [Pip](https://pypi.org/project/pip/)
* [Setuptools](https://pypi.org/project/setuptools/)

### Dependencies
```
dependencies = [
    'importlib-metadata; python_version<"3.8"', "numpy", "pillow", "numba", "line-profiler", "matplotlib"
]
```

The links to get the required dependencies

* [numpy](https://numpy.org/)
* [line-profiler](https://pypi.org/project/line-profiler/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Matplotlib](https://matplotlib.org)

## Installation

To install the package, follow these steps:

1. Clone the git repository containing the source code:  

    git clone https://github.com/ahmetugsuz/Image-filtering.git

2. Navigate to the root directory and run:  

    python3 -m pip install .


## Usage

### Running Tests

#### Unit Tests
To run unit tests:
1. Navigate to the root directory (`image-filtering`).
2. Run the command:  

    python3 -m pytest


#### Runtime Tests
To test runtime:
1. Navigate to the `image-filtering/test` folder.
2. Run the command:  

    python3 -m instapy.timing

This generates a `timing-report.txt` file with the results and prints them in the terminal.

### Deploying

To deploy the package:
1. Navigate to the `image-filtering` folder.
2. Run the command:  

    python3 -m instapy <image_path> <arguments>  

Alternatively:

instapy <image_path> <arguments>

See the full list of arguments using:  

    python3 -m instapy --help


### Examples

Here are some example commands:

* Convert an image to gray:  

    instapy test/rain.jpg --gray


* Apply sepia effect to an image:  

    instapy test/rain.jpg --sepia


* Save the modified image with a specified filename:

    instapy test/rain.jpg --gray -o output_image.jpg

* Scale the image by a factor of 2:  

    instapy test/rain.jpg --sepia -sc 2

`-se` wheras `-se` or `--sepia` will turn it to a sepia filter.

* Adjust sepia effect with numpy implementation:

    instapy test/rain.jpg --sepia -i numpy --effect 0.5


### Equivalent arguments

For convenience, equivalent arguments can be used interchangeably:

* `-g or --gray`: Apply the gray effect.
* `-i or --implementation`: Specify the implementation (e.g., numpy, numba).
* `-r or --runtime`: Measure the runtime of the program.



#### Other deploying examples  

    python3 -m instapy test/rain.jpg -o test_file.jpg -se -sc 0.5 -i numpy   

Will save an image rain called "test_file.jpg" on sepia filter, where it is 2x larger than normal, implemnted/run with numpy.

or

    python3 -m instapy test/rain.jpg --gray -sc 2 -r  

Will show rain image on gray filter where it is half as large, where we also print out the runtime on the terminal.

or   

    instapy test/rain.jpg --sepia -r -i numpy --effect 0.5  

Will run a numpy implementation on the rain image so that it is filtered to 50% effect of the sepia filter from the original, where we also take the runtime of the execution.

### Example Run

Below are examples of the effects applied to the default rain image:

*Rain.jpg (Original):*
![Original Image](https://github.com/ahmetugsuz/Image-filtering/blob/main/test/rain.jpg)

*Rain.jpg (Gray effect, 100% size, 80% intensity, implemented with numba):*
![Gray Effect](https://github.com/ahmetugsuz/Image-filtering/blob/main/grayeffect.jpg)

*Rain.jpg (Sepia effect, 120% size, 100% intensity, implemented with numpy):*
![Sepia Effect](https://github.com/ahmetugsuz/Image-filtering/blob/main/sepiaeffect.jpg)


# Image Filtering Python Package

This README outlines the python package Instapy.

This program allows users to transform an image by applying a vintage sepia or gray effect. The sepia effect creates a warm brownish-grey hue that gives images an aged, antique appearance, while the gray effect converts the image to black and white. The intensity of the desired effect can be adjusted, and the program offers the ability to scale the image. The program implements the filter using customizable options, providing users with control over the final result.

## Prerequisites

You will need the following things properly installed on your computer.

* [Pip](https://pypi.org/project/pip/)
* [setuptools](https://pypi.org/project/setuptools/)

### Dependencies
```
dependencies = [
    'importlib-metadata; python_version<"3.8"', "numpy", "pillow", "numba", "line-profiler", "matplotlib"
]
```

* [numpy](https://numpy.org/)
* [line-profiler](https://pypi.org/project/line-profiler/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Matplotlib](https://matplotlib.org)

## Installation

* `git clone https://github.com/ahmetugsuz/Image-filtering.git` git repository containing the sourcecode
* from the root simply run
* `python3 -m pip install .`

## Running

### Running Tests

#### Unit Tests
* navigate to the root: image-filtering
* `python3 -m pytest` / `pytest`

#### Runtime
* navigate to folder image-filtering/test
* `python3 -m instapy.timing`
  the file `timing-report.txt` will contain the results
  and it would print it out on the terminal

### Deploying

* navigate to folder image-filtering
* `python3 -m instapy <image_path> <arguments>` or `instapy <image_path> <arguments>`
  See full list of arguments using `python3 -m instapy --help`
  `Note:` The `<image_path>` can be "test/rain.jpg" as its the default image who is in the directory, but more images can be added later on if it's preffered.


By writing `instapy test/rain.jpg` you will get the rain image in gray tone since it is on default (you can also give the argument `-g or --gray` to have a gray filter on the image), you switch to sepia by typing `instapy test/rain.jpg -se` wheras `-se` or `--sepia` will turn it to a sepia filter.
If you want to check out all commands or need help, you can type `instapy -h'` or `instapy --help'`.
Note that when you want to save the image, you write `instapy test/rain.jpg -o {filename}.jpg`, here you must state the name of the file you are saving, you must also provide an argument for the command `-sc { float}` which scales the image, or if you want to try out different implementations between `python/numpy/numba`, you must specify which implementation you want with the following command `-i or --implementation`. Remember that `--file` (or `-f`) is required field so you must type in at least `instapy test/rain.jpg` to be able to run the program. If you want to time how long the program takes to execute, you can enter `-r or --runtime` without any arguments. The program has also been extended so that you can enter effects on a sepia image that are implemented with numpy, of which you give a `k` value of how much effect you want between 0-1 which corresponds to 0-100%. If you want to adjust the effect of sepia, you can enter `instapy test/rain.jpg -se -i numpy -e {effect/k: float}`.

#### deploying examples
`python3 -m instapy test/rain.jpg -o test_file.jpg -se -sc 0.5 -i numpy`
Will save an image rain called "test_file.jpg" on sepia filter, where it is 2x larger than normal, implemnted/run with numpy.

or

`python3 -m instapy test/rain.jpg --gray -sc 2 -r`
Will show rain image on gray filter where it is half as large, where we also print out the runtime on the terminal.

or 

`instapy test/rain.jpg --sepia -r -i numpy --effect 0.5`
Will run a numpy implementation on the rain image so that it is filtered to 50% effect of the sepia filter from the original, where we also take the runtime of the execution.

### Example Run
Here is a look at how it appears on the default rain picture:
    
Rain.jpg (Original/default image):   
![alt text](https://github.com/ahmetugsuz/Image-filtering/blob/main/test/rain.jpg)

Rain.jpg (Gray effect, size 100%, 80% gray effect, implemented with numba)
![alt text](https://github.com/ahmetugsuz/Image-filtering/blob/main/grayeffect.jpg)

Rain.jpg (Sepia effect, resized scale 20% larger, 100% sepia effect, implemented with numpy): 
![alt text](https://github.com/ahmetugsuz/Image-filtering/blob/main/sepiaeffect.jpg)

