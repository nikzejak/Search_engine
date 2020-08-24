
class TrieNode(object):

    def __init__(self, char: str):
        self.dictionary = {}
        self.children = []
        self.char = char
        self.word_finished = False

    @staticmethod
    def dodavanje(root, word: str, link):

        node = root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.word_finished = True

        if link in node.dictionary:
            node.dictionary[link] += 1
        else:
            node.dictionary[link] = 1

    @staticmethod
    def pretraga(root, words: str):

        node = root
        if not root.children:
            return False, 0
        for char in words:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return {}

        if not node.word_finished:  # if node.word_finished == False:
            return None

        return node.dictionary
