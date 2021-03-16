#!/usr/bin/env python

import sys
def add_num(a,b):
    sum=a+b;
    return sum; 

numa = int( sys.argv[1] )
numb = int( sys.argv[2] )
print("La somme est : ",add_num(numa,numb))
print(sys.argv)


