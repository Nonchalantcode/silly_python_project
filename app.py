#!/usr/bin/env python

import cowsay
import sys

cli_args = sys.argv[1:]

if len(cli_args):
   (v,) = cli_args
   cowsay.cow("Cow says: {}".format(v))
else:
   cowsay.cow('Hello, world')
    

