import sys
sys.path.append('../')

from src.trie import TrieNode, insert
import unittest

class TestTrie(unittest.TestCase):
    # Testing Strategy:
    # 1. word length (0, 1, >1)
    # 2. two words with first (0, 1, >1) characters shared 

    def width_one_branch_check(self, root, letters):
        # Checks that a path through trie (every node in path only has 1 child) matches given letters
        node = root
        for letter in letters:
            self.assertEqual(len(node.children), 1)
            self.assertEqual(node.children[0].c, letter)
            node = node.children[0]

        self.assertTrue(node.done)

    def test_single_word(self):
        root = TrieNode('')
        insert(root, 'abc', 3)
        self.width_one_branch_check(root, 'abc')

    def test_disjoint_words(self):
        root = TrieNode('')
        insert(root, 'abc', 3)
        insert(root, 'bcd', 3)
        self.assertEqual(len(root.children), 2)

        # Test abc branch
        node = None
        for child in root.children:
            if child.c == 'a':
                node = child
                break
        self.assertTrue(node is not None)

        self.width_one_branch_check(node, 'bc')

        # test bcd branch
        node = None
        for child in root.children:
            if child.c == 'b':
                node = child
                break
        
        self.assertTrue(node is not None)
        self.width_one_branch_check(node, 'cd')

    def test_first_char_shared(self):
        root = TrieNode('')
        insert(root, 'abc', 3)
        insert(root, 'acd', 3)

        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].c, 'a')

        node = root.children[0]

        self.assertEqual(len(node.children), 2)
        
        # test bc branch
        child = None
        for candidate_child in node.children:
            if candidate_child.c == 'b':
                child = candidate_child
                break

        self.assertEqual(len(child.children), 1)
        self.assertEqual(child.children[0].c, 'c')
        self.assertTrue(child.children[0].done)

        # test cd branch
        child = None
        for candidate_child in node.children:
            if candidate_child.c == 'c':
                child = candidate_child
                break

        self.assertEqual(len(child.children), 1)
        self.assertEqual(child.children[0].c, 'd')
        self.assertTrue(child.children[0].done)

    def test_first_few_chars_shared(self):
        root = TrieNode('')
        insert(root, 'abc', 3)
        insert(root, 'abd', 3)

        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].c, 'a')

        root = root.children[0]

        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].c, 'b')

        root = root.children[0]

        self.assertEqual(len(root.children), 2)
        children_cs = [child.c for child in root.children]
        self.assertTrue('c' in children_cs and 'd' in children_cs)

if __name__ == '__main__':
    unittest.main()
