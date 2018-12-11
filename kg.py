#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-

# kg-ot és dkg-ot alakít át grammá.

__author__ = "Zsolt Pető"
__license__ = "MIT"
__version__ = "0.2"

import sys
import os


c = 4
z = 0

os.system('clear')
print("-" * 80)
print("Szia Milán !".center(80))
print("Ez a kis program segít megérteni a kiló(kg) és a deka(dkg) fogalmát.".center(80))

def ellenorzes ():
    while True:
        try:
            i = float(input("Írd be azt a számot, amit át szeretnél alakítani, és nyomj egy ENTER-t. (Pl.: 2.5, 3, 4.18): "))
            if i < 0:
               i = 0
            else:
                pass
            y = c/i
            break
        except ValueError:
                print("Ez nem egy szám! Lehet hogy félre ütöttél valamit :-)".center(80))
        except ZeroDivisionError:
            print("A beírt szám nulla vagy negatív! Lehet hogy félre ütöttél valamit :-)".center(80))
    e = i * v
    os.system('clear')
    print("-" * 80)
    print("-" * 80)
    print("")
    print("                Az átalakított szám:", e, "gramm")
    print("")
    print("-" * 80)


try:
    while True:
        z = 0
        while [z != 1]:
            print("-" * 80)
            print("A 'Ctrl-c'-re megszakítja a programot és kilép.".center(80))
            print("-" * 80)
            print("Válassz a két lehetőség közül.".center(80))
            print("-" * 80)
            try:
                x = int(input("Mit szeretnél grammá alakítani?\nÍrd be a számot és nyomj egy ENTER-t.\n[1] kg vagy [2] dkg : "))
                if x in range(1,3):
                    z = 1
                    if x == 1:
                        v = 1000
                    else:
                        v = 10
                    ellenorzes()
                    pass
                else:
                    os.system('clear')
                    print("-" * 80)
                    print("-" * 80)
                    print("")
                    print("Nem jó számot választottál 1-est és a 2-est lehet választani!".center(80))
                    print("")
                    print("-" * 80)
                    z = 0
            except ValueError:
                os.system('clear')
                print("-" * 80)
                print("-" * 80)
                print("")
                print("Ez nem szám amit beírtál. Vagy nem egész számot írtál be!".center(80))
                print("")
                print("-" * 80)
                z = 0
            except KeyboardInterrupt:  # control-c -re kilép a programból
                sys.exit(0)


except KeyboardInterrupt:
    pass
