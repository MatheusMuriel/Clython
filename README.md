# Clython
Estudo de desenvolvimento de CLI usando Python


## Argparser
Faz soma de 2 numeros
````
λ python ArgParse.py
usage: ArgParse.py [-h] [--sum] N [N ...]
ArgParse.py: error: the following arguments are required: N

λ python ArgParse.py -h
usage: ArgParse.py [-h] [--sum] N [N ...]

Add some integers.

positional arguments:
  N           interger list

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)

λ python ArgParse.py --sum 40 32
72
````

