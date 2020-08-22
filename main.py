import os
from parser2 import Parser
from trie import TrieNode

global parser
parser = Parser()
trie = TrieNode(-1)


def opcija1():

    global trie
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
                    # print()
                    # print(links)
                    # print(words)
                    file = os.path.join(dirpath, f)
                    # print(file)
                    for word in parser.words:
                        trie.dodavanje(trie, word.lower(), file)

        mainMenu()


def opcija2():

    global reci_za_pretragu;
    reci_za_pretragu = input("Unesite rec(i) za pretragu...\n-> ")

    if len(reci_za_pretragu.split()) == 3:
        if reci_za_pretragu.split()[1] == 'OR' or reci_za_pretragu.split()[1] == 'or':
            print("OR je tu -> UNIJA")
        elif reci_za_pretragu.split()[1] == 'AND' or reci_za_pretragu.split()[1] == 'and':
            print("AND je tu -> PRESEK")
        elif reci_za_pretragu.split()[1] == 'NOT' or reci_za_pretragu.split()[1] == 'not':
            print("NOT je tu -> KOMPLEMENT")
    else:
        print("Pretraga kada nema operacija ili kada ima vise ili manje od tri reci")
        print(trie.pretraga(trie, reci_za_pretragu))
    print(reci_za_pretragu.split())

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
