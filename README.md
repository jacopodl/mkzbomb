# mkZbomb
mkZbomb is simple python script that generate ZipBomb of desired dimension.

# Getting the code
Download from repository:

    $ git clone https://github.com/jacopodl/mkzbomb
    $ cd mkzbomb

or install from pip:
    
    $ pip install mkzbomb
    
# How to use
                _     _______                     _
               | |   |___  / |                   | |
      _ __ ___ | | __   / /| |__   ___  _ __ ___ | |__
     | '_ ` _ \| |/ /  / / | '_ \ / _ \| '_ ` _ \| '_ \
     | | | | | |   <  / /__| |_) | (_) | | | | | | |_) |
     |_| |_| |_|_|\_\/_____|_.__/ \___/|_| |_| |_|_.__/


    usage: mkzbomb.py [-h] [--layer LAYER] [--cps CPS] [--size SIZE] name

    Build ZipBomb.

    positional arguments:
      name           Output name

    optional arguments:
      -h, --help     show this help message and exit
      --layer LAYER  Set zbomb deep
      --cps CPS      Copies for each layer
      --size SIZE    Set size of 'zero' file (Size in KB)
    
    $> python mkzbomb.py SimpleBomb.zip
    $> python mkzbomb.py SimpleBomb.zip --layer 18
 
# Warning
Building(or storing) ZipBomb on Windows system with Windows Search service enabled can bring system to instability issue.
    
# License
See LICENSE
