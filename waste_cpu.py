# To run: python waste_cpu.py &
# Use kill to terminate

# Requirement: pigz
# Make sure you put /tmp on tmpfs
# Otherwise not good for your storage

# I bought a new battery for my laptop
# and need to discharge the battery for a few times
# I wrote a small script to call pigz on some random data

# https://stackoverflow.com/questions/41059606/wasting-cpu-cycles-with-python
# https://stackoverflow.com/questions/14275975/creating-random-binary-files

import os
import time

slowness = 10
fname='/tmp/random.bin'

if os.path.exists(fname):
  os.remove(fname)

if os.path.exists(fname+".gz"):
  os.remove(fname+".gz")

with open(fname, 'wb') as fout:
  fout.write(os.urandom(slowness*1024*1024))

while True:
  os.system ("pigz --keep " +fname)
  os.remove(fname+".gz")

