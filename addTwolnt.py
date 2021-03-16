#!/usr/bin/env python

import sys

def add_num(a,b):
    sum=a+b;
    return sum; 

conti = 1
if len(sys.argv) >= 4 :
    print('Vous avez renseigne plus de 2 parametres')
    conti = 0

if len(sys.argv) <= 2 :
    print('Vous avez renseigne moins de 2 parametres')
    conti = 0

if conti == 1: #ceci est pour prevenir l'erreur qui peut se creer si nous avons moins de parametres,
    numa = int( sys.argv[1] )
    numb = int( sys.argv[2] )
    print("La somme est : ",add_num(numa,numb))
    print(sys.argv)

