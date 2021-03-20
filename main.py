#!/usr/bin/env python

import sys


def main():
    print("Faite le choix de votre operation 1 ou 2 ?")
    print("1 pour Addition")
    print("2 pour Multiplication") 
    choix = input(" Votre choix: ")
    if choix == 1:
        from addTwolnt import main
    if choix == 2:
	from mulTwoInt import mul

main()
