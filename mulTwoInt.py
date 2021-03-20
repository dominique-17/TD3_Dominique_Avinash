#!/usr/bin/env python

import sys

def add_mul(a,b):
    sum=a*b;
    return sum; 
    
def mul():
    conti = 1
    if len(sys.argv) >= 4 :
        print('Vous avez renseigne plus de 2 parametres')
        conti = 0

    if len(sys.argv) < 3 :
        print('Vous avez renseigne moins de 2 parametres')
        conti = 0

    if len(sys.argv) == 2:
        num2 = input(" entrer le nombre 2: ")
        print("Le produit est : ",add_mul(int( sys.argv[1] ),num2))
    if len(sys.argv) == 1:
        num1 = input(" entrer le nombre 1: ")
        num2 = input(" entrer le nombre 2: ")
        print("Le produit est : ",add_mul(num1,num2))
    
    if conti == 1: #ceci est pour prevenir l'erreur qui peut se creer si nous avons moins de parametres,
        numa = int( sys.argv[1] )
        numb = int( sys.argv[2] )
        print("Le produit est : ",add_mul(int( sys.argv[1] ),int( sys.argv[2] )))
        print(sys.argv)

mul()
