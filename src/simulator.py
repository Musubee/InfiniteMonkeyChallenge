# The Simulator class will produce random characters, check them against a trie, and present information on the current status of the challenge

import random
class Simulator:
    def __init__(self, trie: dict[str, dict|int|bool], valid_elements: str|list[str]):
        self.trie = trie
        self.curr_node = trie
        self.valid_elements = valid_elements
        self.done = False

    def next(self) -> tuple[str, int] | tuple[None, None]:
        # Gets a random character and returns the generated character and updated completion percentage
        if self.done:
            return (None, None)

        next_element = random.choice(self.valid_elements)
        if next_element in self.curr_node:
            self.curr_node = self.curr_node[next_element]
        else:
            self.curr_node = self.trie

        if self.curr_node['is_done']:
            self.done = True

        return (next_element, self.curr_node['max_percentage'])

    def get_current_percentage(self) -> int:
        return self.curr_node['max_percentage']
