# https://www.youtube.com/watch?v=f3D-w6XMTN8
def mainMenu():
    print("1. Opcija 1")
    print("2. Opcija 2")
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


def opcija1():
    print("Ovo je opcija 1")
    a = input("\nPritisnite enter za povratak u glavni meni")
    mainMenu()


def opcija2():
    print("Ovo je opcija 2")
    a = input("\nPritisnite enter za povratak u glavni meni")
    mainMenu()


mainMenu()