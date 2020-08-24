import os
from parser2 import Parser
from trie import TrieNode

global parser
parser = Parser()
trie = TrieNode(2)


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
    s = {"OR", "or", "AND", "and", "NOT", "not"}

    if (len(reci_za_pretragu.split()) == 3) and (reci_za_pretragu.split()[1] in s):
        if reci_za_pretragu.split()[1] == 'OR' or reci_za_pretragu.split()[1] == 'or':
            if (reci_za_pretragu.split()[0] == 'OR') or (reci_za_pretragu.split()[2] == 'OR'):
                print("Prva i treca rec ne smeju biti OR")
            else:
                print("OR je prisutan")
                if (trie.pretraga(trie, reci_za_pretragu.split()[0])) or (trie.pretraga(trie, reci_za_pretragu.split()[2])):
                    print("Prva rec -> " + reci_za_pretragu.split()[0].upper())
                    print(trie.pretraga(trie, reci_za_pretragu.split()[0]))
                    print("Druga rec -> " + reci_za_pretragu.split()[2].upper())
                    print(trie.pretraga(trie, reci_za_pretragu.split()[2]))

        elif reci_za_pretragu.split()[1] == 'AND' or reci_za_pretragu.split()[1] == 'and':
            if (reci_za_pretragu.split()[0] == 'AND') or (reci_za_pretragu.split()[2] == 'AND'):
                print("Prva i treca rec ne smeju biti AND")
            else:
                print("AND je prisutan")
                if (trie.pretraga(trie, reci_za_pretragu.split()[0])) and (trie.pretraga(trie, reci_za_pretragu.split()[2])):
                    print("Prva rec: " + reci_za_pretragu.split()[0].upper())
                    print(trie.pretraga(trie, reci_za_pretragu.split()[0]))
                    print("Druga rec: " + reci_za_pretragu.split()[2].upper())
                    print(trie.pretraga(trie, reci_za_pretragu.split()[2]))
                else:
                    if (trie.pretraga(trie, reci_za_pretragu.split()[0])) == {}:
                        print("Prva rec nije pronadjena!\nMolimo unesite nove reci...\n")
                    elif (trie.pretraga(trie, reci_za_pretragu.split()[2])) == {}:
                        print("Druga rec nije pronadjena!\nMolimo unesite nove reci...\n")

        elif reci_za_pretragu.split()[1] == 'NOT' or reci_za_pretragu.split()[1] == 'not':
            if (reci_za_pretragu.split()[0] == 'NOT') or (reci_za_pretragu.split()[2] == 'NOT'):
                print("Prva i treca rec ne smeju biti NOT")
            else:
                print("NOT je prisutan")
                if (trie.pretraga(trie, reci_za_pretragu.split()[0]) != {}) and (trie.pretraga(trie, reci_za_pretragu.split()[2]) == {}):
                    print("Rec -> " + reci_za_pretragu.split()[0].upper())
                    print(trie.pretraga(trie, reci_za_pretragu.split()[0]))
                else:
                    print("Druga rec -> " + reci_za_pretragu.split()[2].upper() + " je prisutna u pretrazi.\nDa bi NOT "
                                                                               "funkcionisao, molimo unesite nove reci..."
                                                                               "\nNAPOMENA: NOT funkcionise kada je samo"
                                                                               " prva rec prisutna u pretrazi, a druga ne!")
                    # print("Rec -> " + reci_za_pretragu.split()[0].upper())
                    # print(trie.pretraga(trie, reci_za_pretragu.split()[0]))
                    print()
    else:
        print("Pretraga jedne ili vise od 3 reci:")
        for wor in reci_za_pretragu.split():
            print(wor)
            print(trie.pretraga(trie, wor))
            print()
        # print(trie.pretraga(trie, reci_za_pretragu))

    # print(reci_za_pretragu.split())

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
