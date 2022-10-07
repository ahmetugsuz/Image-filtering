# INSTAPY

## English

### What does the package do
This package takes an image and adds a gray or sepia filter to the image. In this package we have specific image 'rain.jpg' which we illustrate how the filter looks like, together with that the package has various implementations such as pure python, numpy and numba, where each implementation has varying speed of runtime.

### How to install the package
The package can be installed by cloning the git directory
`git clone https://github.uio.no/IN3110/IN3110-ahmettu.git`
With this you will have the root folder `IN3110-ahmettu` in your directory.
Here you can continue to where the package is located: `cd IN3110-ahmettu/assignment3`.
From your local cloned repo directory you can now run:
`pip install .` when you are inside in the `assignment3` folder.

In order to run this package you need to have some libraries installed, this is required libraries that is put on dependencies:
```
dependencies = [
    'importlib-metadata; python_version<"3.8"', "numpy", "pillow", "numba", "line-profiler", "matplotlib"
]
```
You can install all of these dependencies if you have pip installed or anoconda, with newest update of pip, will `pip install .` work fine to install all.
You also need to have python-version older than 3.7 (it can be 3.7).

### How to run the package
You can easily run the package by running `python3 -m instapy <arguments>` or `instapy <arguments>` on terminal.
By writing `instapy test/rain.jpg` you will get the rain image in gray tone since it is on default (you can also give the argument `-g or --gray` to have a gray filter on the image), you switch to sepia by typing `instapy test/rain.jpg -se` wheras `-se` or `--sepia` will turn it to a sepia filter.
If you want to check out all commands or need help, you can type `instapy -h'` or `instapy --help'`.
Note that when you want to save the image, you write `instapy test/rain.jpg -o {filename}.jpg`, here you must state the name of the file you are saving, you must also provide an argument for the command `-sc { float}` which scales the image, or if you want to try out different implementations between `python/numpy/numba`, you must specify which implementation you want with the following command `-i or --implementation`. Remember that `--file` (or `-f`) is required field so you must type in at least `instapy test/rain.jpg` to be able to run the program. If you want to time how long the program takes to execute, you can enter `-r or --runtime` without any arguments. The program has also been extended so that you can enter effects on a sepia image that are implemented with numpy, of which you give a `k` value of how much effect you want between 0-1 which corresponds to 0-100%. If you want to adjust the effect of sepia, you can enter `instapy test/rain.jpg -se -i numpy -e {effect/k: float}`.

#### driving example
`python3 -m instapy test/rain.jpg -o test_file.jpg -se -sc 0.5 -i numpy`
Will save an image rain called "test_file.jpg" on sepia filter, where it is 2x larger than normal, implemnted/run with numpy.

or

`python3 -m instapy test/rain.jpg --gray -sc 2 -r`
Will show rain image on gray filter where it is half as large, where we also print out the runtime on the terminal.

or 

`instapy test/rain.jpg --sepia -r -i numpy --effect 0.5`
Will run a numpy implementation on the rain image so that it is filtered to 50% effect of the sepia filter from the original, where we also take the runtime of the execution.


## Norsk

### Hva gjør pakken
Denne pakken tar et bilde og legger til et grå eller et sepia filter på bilde. I denne pakken har vi bestemt bilde 'rain.jpg' som vi illustrerer hvordan filter ser ut, sammen med det har pakken ulike implemntasjoner som pure python, numpy og numba, hvor hver implementasjon har varierende hastighet på kjøretid. 

### Hvordan installere pakken
Pakken kan bli installert ved å klone git directory 
`git clone https://github.uio.no/IN3110/IN3110-ahmettu.git`
Hermed vil du ha root mappen `IN3110-ahmettu`. 
Her kan du videre inn til hvor pakken ligger: `cd IN3110-ahmettu/assignment3`.
Fra din lokale klonet repo directory kan du kjøre nå: 
`pip install .` når du er inne på mappen `assignment3`. 

For å kjøre denne pakken må du ha noen biblioteker installert, dette er nødvendige biblioteker som er satt på dependencies:
```
dependencies = [
     'importlib-metadata; python_version<"3.8"', "numpy", "pillow", "numba", "line-profiler", "matplotlib"
]
```
Du kan installere alle disse dependencies hvis du har pip installert eller anoconda, med nyeste oppdatering av pip, vil `pip install .` fungere fint for å installere alle.
Du må også ha python-versjon eldre enn 3.7 (det kan være 3.7).

### Hvordan kjøre pakken
Du kan enkelt kjøre pakken ved å kjøre `python3 -m instapy <argumenter>` eller `instapy <argumenter>` på terminal.
Ved å skrive `instapy test/rain.jpg` vil du få ut rain bildet på grå tone siden den er på default (du kan også gi argumentet `-g or --gray` til å ha grå filter på bilde), dette kan du bytte til sepia ved å skrive inn `instapy test/rain.jpg -se`.
Hvis du har lyst til å sjekke ut alle komandoer eller trenger hjelp kan du skrive `instapy -h` eller `instapy --help`.
Legg merke til at når du vil lagre bildet så skriver du `instapy test/rain.jpg -o {filename}.jpg`, her må du oppgi hva den filen du lagrer heter, du må også gi argument for kommandoen `-sc {float}` som skalerer bilde, eller hvis du vil prøve ut ulike implementasjoner mellom `python/numpy/numba` må du oppgi hvilken implementasjon du vil ha med følgende kommando `-i or --implementation`. Hvis du vil ta tida på hvor lang tid programmet tar for å eksekvere kan du taste inn `-r or --runtime` uten noe argumenter. Programmet er også utvidet slik at du kan oppgi effecten på sepia bilde som er implementer med numpy, hvorav du gir en `k` verdi på hvor mye effect du vil ha mellom 0-1 som tilsvarer 0-100%. Om du vil justere på effekten av sepia kan du oppgi `instapy test/rain.jpg -se -i numpy -e {effect/k}`.


#### kjøreeksempel
`python3 -m instapy test/rain.jpg -o test_file.jpg -se -sc 0.5 -i numpy`
Vil lagre et bilde rain kalt "test_file.jpg" på sepia filter, hvor den er dobbelt så større enn normalt, kjørt med numpy.

eller

`python3 -m instapy test/rain.jpg --gray -sc 2 -r`
Vil vise rain bilde på grå filter hvor den er halvparten så stor, der vi også printer ut kjøretiden på terminalen.

eller 

`instapy test/rain.jpg --sepia -r -i numpy --effect 0.5`
Vil kjøre et numpy implementasjon på rain bilde slik at det er filterert i 50% effekt av sepia filter fra orginalen, hvor vi også tar kjøretiden på eksekveringen.