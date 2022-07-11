class Solution(object):


    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        class Node:

            def __init__(self):
                self.links = {}  # is a dictionary where key is a char and value is a child node
                self.is_end = False

            # get links initiating from char
            def get(self, char):
                return self.links[char]

            def has(self, char):
                return char in self.links.keys()

            def put(self, char, node):
                self.links[char] = node

            def __repr__(self):
                str_ret = ' - '.join(self.links.keys())
                return str_ret


        class Trie():
            trie_root = None  # Node

            def __init__(self):
                self.trie_root = Node()

            def add(self, new_word):
                node = self.trie_root
                for c in new_word:
                    if not c in node.links.keys():  # or keys is empty
                        node.put(c, Node())
                    node = node.get(c)
                node.is_end = True

            def get_min_prefix(self, word):
                node = self.trie_root
                min_pref = ''
                for c in word:
                    if node.has(c):
                        min_pref += c
                        node = node.get(c)
                        if node.is_end:
                            break
                    else:
                        min_pref = ''
                        break
                return min_pref

            def get_node_links_repr_recursive(self, node):
                str_ret = f'{node}\n'
                for node in node.links.values():
                    str_ret += self.get_node_links_repr_recursive(node)
                return str_ret

            def __repr__(self):
                return self.get_node_links_repr_recursive(self.trie_root)


        trie = Trie()
        for each_str in dictionary:
            trie.add(each_str)
        print(trie)

        ret_str = ''
        for each_str in sentence.split():
            min_pref = trie.get_min_prefix(each_str)
            ret_str += ' ' + (min_pref if len(min_pref) > 0 else each_str)
            ret_str = ret_str.strip()

        return ret_str



