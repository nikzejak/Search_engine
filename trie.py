# referenca
# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

class TrieNode(object):

    def __init__(self, char: str):
        self.dictionary = {}
        self.children = []
        self.char = char
        self.word_finished = False

    @staticmethod
    def dodavanje(root, word: str, link):

        node = root
        for char in word:       # prolazimo kroz sve karaktere reci
            found_in_child = False  # da li rec vec postoji u stablu
            for child in node.children:  # prolaz kroz sve potomke stabla
                if child.char == char:
                    node = child
                    found_in_child = True   # postoji u stablu, pa iskoci iz petlje
                    break
            if not found_in_child:  # ako nismo pronasli rec u stablu
                new_node = TrieNode(char)   # kreira se novi cvor
                node.children.append(new_node)  # dodajemo novi cvor u stablo
                node = new_node     # povezujemo sa novim cvorom
        node.word_finished = True   # oznacava kraj i da je rec dodata u stablo

        if link in node.dictionary:
            node.dictionary[link] += 1   # uveca se svaki put kada pronadjemo rec da se ponavlja na stranici
        else:
            node.dictionary[link] = 1

    @staticmethod
    def pretraga(root, words: str):

        node = root
        if not root.children:   # ako ne postoje potomci, izlazimo iz programa
            return False, 0
        for char in words:
            char_not_found = True
            for child in node.children:     # pretrazujemo sve potomke u stablu
                if child.char == char:      # ako je pronadjena rec u stablu
                    char_not_found = False
                    node = child            # dodeljujemo cvor kao potomka
                    break
            if char_not_found:              # ukoliko nismo nista pronasli vracamo prazan recnik
                return {}

        # if not node.word_finished:  # if node.word_finished == False:
        #     return None

        return node.dictionary
