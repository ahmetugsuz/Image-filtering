# Instapy

This README outlines the python package Instapy.

This application is able to run grayscale and sepia image of a given input image.
The filtering can be done using implementations done with either Python, Numba or Numpy;
detailing runtime and comparisons between them

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

Rain.jpg (Original image):
![alt text](https://github.com/ahmetugsuz/Image-filtering/blob/master/test/rain.jpg)

