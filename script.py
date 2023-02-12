#!/usr/bin/python3

import sys
"""This gives the total number of arguments
Args:
    len (int): len
"""
# Total number of arguments
print('Total arguments:', len(sys.argv))

print("Argument values are:")

# Iterate command-line arguments using for loop

for i in sys.argv:
    print(i)
