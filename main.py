import os
from parser2 import Parser

global parser
parser = Parser()


def opcija1():

    global putanja
    putanja = str(input("Unesite apsolutnu putanju direktorijuma: "))

    if not os.path.exists(putanja):
        print("Putanja ne postoji! Molimo unesite novu...")
        opcija1()
    else:
        for dirpath, dirnames, filenames in os.walk(putanja):
            for f in filenames:
                if f.endswith('.html') or f.endswith('.htm'):
                    # print("\nFiles:", f)
                    # print("\n" + os.path.join(dirpath, f))
                    # print(parser.parse(os.path.join(dirpath, f)))
                    links, words = parser.parse(os.path.join(dirpath, f))
                    print()
                    print(links)
                    print(words)
        mainMenu()


def opcija2():
    print("Ovo je opcija 2")
    print(putanja)
    a = input("\nPritisnite enter za povratak u glavni meni")
    mainMenu()


# https://www.youtube.com/watch?v=f3D-w6XMTN8
def mainMenu():
    print("1. Unos direktorijuma")
    print("2. Pretraga reci")
    print("3. Exit")

    while True:
        try:
            selekcija = int(input("Unesite Vas izbor: "))
            if selekcija == 1:
                opcija1()
                break
            elif selekcija == 2:
                opcija2()
                break
            elif selekcija == 3:
                break
            else:
                print("Uneli ste pogresan broj! Unesite brojeve 1-3\n")
                mainMenu()
        except ValueError:
            print("Neispravan unos! Unesite brojeve 1-3\n")
    exit


mainMenu()
