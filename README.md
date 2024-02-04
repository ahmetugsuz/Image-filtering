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
### Required dependencies
You will be guided through how to install the requirements later on on this documentation (see. Installation, point 3.)

* [numpy](https://numpy.org/)
* [line-profiler](https://pypi.org/project/line-profiler/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Matplotlib](https://matplotlib.org)

## Installation

### Installing the Package

To install the package, follow these steps:

1. Clone the git repository containing the source code:  
```bash 
git clone https://github.com/ahmetugsuz/Image-filtering.git
```    

2. Navigate to the root directory:
```bash 
cd image-filtering
```    

3. Install the package and its dependencies:
```bash 
python3 -m pip install .
```   
After making any changes to the package, it's essential to reinstall it to ensure that the changes take effect. Use the same command above to reinstall the package.  

### Installing Requirements

If all dependencies is not installed properly by `python3 -m pip install .`, you'll need to install the required Python packages listed in the `requirements.txt` file.

#### Locally

If you're not using a virtual environment, you can install the project dependencies directly using pip:

```bash
pip install -r requirements.txt
```

This command will install all the necessary packages globally on your system.

#### Using a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies and isolate them from other projects. 
If you haven't already, you can create a virtual environment using venv:  

    python -m venv myenv   

* On macOS/Linux:
```bash
source myenv/bin/activate
```

* On Windows:  
```bash
myenv\Scripts\activate
```

Once the virtual environment is activated, you can install the project dependencies using pip:  
```bash
pip install -r requirements.txt
```


## Usage

### Deploying

To deploy the package:
1. Navigate to the `image-filtering` folder (if youre not at the root of the project):
```bash 
cd image-filtering
```    

2. Base command to apply a filter or converting a image:  
```bash
python3 -m instapy <image_path> <arguments>  
```  
Where you will need to pass arguments for `<image_path>` and `<arguments>`  

Alternatively:
```bash
instapy <image_path> <arguments>
```  

Where you need to pass arguments for `<image_path>` and `<arguments>`   

See the full list of arguments, using:  
```bash 
python3 -m instapy --help
```   

### Examples

Here are some example commands with the default image that follows with this package rain.jpg:

* Convert an image to gray:  
```bash
instapy test/rain.jpg --gray
```   

* Apply sepia effect to an image:  
```bash 
instapy test/rain.jpg --sepia
```

* Save the modified image with a specified filename:
```bash 
instapy test/rain.jpg --gray -o output_image.jpg
```    

* Scale the image by a factor of 2:  
```bash 
instapy test/rain.jpg --sepia -sc 2
```  

`-se` wheras `-se` or `--sepia` will turn it to a sepia filter.

* Adjust sepia effect with numpy implementation:
```bash 
instapy test/rain.jpg --sepia -i numpy --effect 0.5
```   

### Equivalent arguments

For convenience, equivalent arguments can be used interchangeably:

* `-g or --gray`: Apply the gray effect.
* `-i or --implementation`: Specify the implementation (e.g., numpy, numba).
* `-r or --runtime`: Measure the runtime of the program.

**Important Note:**
The primary purpose of this package is to enable users to apply filters to any image of their choice. To achieve this, you need to provide the path to the image you wish to modify. By default, the image is located at `test/rain.jpg`, but you have the flexibility to place it anywhere on your system.

**Usage Instructions:**
When passing arguments to the package, ensure that you specify the exact path to the image, including its name and file extension. For example, if your image is located in a directory named `images` and is named `my_image.jpg`, you would provide the following path:
`../path_to_image/images/my_image.jpg`

By following these instructions, you can seamlessly apply filters to any image, regardless of its location on your system.


### Running Tests

#### Unit Tests
To run unit tests:
1. Navigate to the root directory (`image-filtering`)
2. Run the command:  
```bash 
python3 -m pytest
```   

#### Runtime Tests
To test runtime:
1. Make sure you located at the root of the project `image-filtering`, if not:
```bash 
cd image-filtering
```   

2. Run the command:  
```bash 
python3 -m instapy.timing
```   

#### Runtime Comparison

Upon execution, the program generates a `timing-report.txt` file and displays the results in the terminal. This report compares the performance of different Python libraries, including:

* **Numba (Numerical Python):** A fundamental package for scientific computing in Python.
* **NumPy (Numpy-accelerated):** A just-in-time compiler for Python that speeds up numerical computations.

The comparison helps users understand the runtime differences when applying filters using these libraries. Results are provided both in the `timing-report.txt` file and printed directly in the terminal for easy analysis.


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



## Contributing:
Contributions to the project are welcome! Please contact me on my website: [ahmettu.com](https://ahmettu.com)  

## License:
This project is licensed under the MIT License. See the LICENSE file for more details.