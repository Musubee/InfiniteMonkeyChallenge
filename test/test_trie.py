import sys
sys.path.append('../')

from src.trie import create_trie
import unittest

class TestTrie(unittest.TestCase):
    # Testing Strategy:
    # 1. word length (0, 1, >1)
    # 2. two words with first (0, 1, >1) characters shared 

    def one_word_check(self, root, letters, orig_length):
        # Checks that a path through trie (every node in path only has 1 child) matches given letters
        node = root
        start_offset = orig_length - len(letters)
        for i, letter in enumerate(letters, start_offset):
            self.assertTrue(letter in node)
            self.assertEqual(node['max_percentage'], round((i/orig_length * 100), 2))
            self.assertFalse(node['is_done'])
            node = node[letter]

        self.assertTrue(node['is_done'])

    def test_single_word(self):
        works = ['abc']
        trie = create_trie(works)
        self.one_word_check(trie, 'abc', 3)

    def test_disjoint_words(self):
        works = ['abc', 'bcd']
        trie = create_trie(works)
        self.one_word_check(trie, 'abc', 3)
        self.one_word_check(trie, 'bcd', 3)

    def test_first_char_shared(self):
        works = ['abc', 'acd']
        trie = create_trie(works)
        self.assertTrue('a' in trie)
        new_root = trie['a']
        self.one_word_check(new_root, 'bc', 3)
        self.one_word_check(new_root, 'cd', 3)

    def test_first_few_chars_shared(self):
        works = ['abc', 'abd']
        trie = create_trie(works)
        self.assertTrue('a' in trie and 'b' in trie['a'])
        
        new_root = trie['a']['b']
        self.one_word_check(new_root, 'c', 3)
        self.one_word_check(new_root, 'd', 3)

    def test_overlapping_words(self):
        works = ['ab', 'abcd']
        trie = create_trie(works)
        self.assertTrue(('a' in trie and 'b' in trie['a'] and 
                        'c' in trie['a']['b'] and 'd' in trie['a']['b']['c']))
        self.assertEqual(trie['a']['max_percentage'], 50.00)
        self.assertEqual(trie['a']['b']['max_percentage'], 100.00)
        self.assertTrue(trie['a']['b']['is_done'])
        self.assertEqual(trie['a']['b']['c']['max_percentage'], 75.00)
        self.assertEqual(trie['a']['b']['c']['d']['max_percentage'], 100.00)
        self.assertTrue(trie['a']['b']['c']['d']['is_done'])

if __name__ == '__main__':
    unittest.main()
