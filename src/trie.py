# Use a Trie to test whether the simulation is matching the works of Shakespeare
# Implemented recursively, each node will contain its value, children, and the largest percentage match for the current prefix

# TODO:
# 1. Add capability for Trie to work at word-level granularity (each node is a word; save this task for later)

# annotation import allows recursive type-hinting, would otherwise throw error at children: List[TrieNode] on line 9
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

@dataclass
class TrieNode:
    c: str
    max_percentage: int = 0
    done: bool = False
    children: List[TrieNode] = field(default_factory=list)

def insert(root: TrieNode, suffix: str, orig_len: int) -> None:
    # inserts suffix string into root
    assert len(suffix) > 0, 'Cannot operate on empty string'
    assert root is not None, 'Cannot operate on empty Trie'

    child = None
    letter = suffix[0]
    for candidate_child in root.children:
        if candidate_child.c == letter:
            child = candidate_child
            break

    if child is None:
        child = TrieNode(letter)
        root.children.append(child)
    
    percentage_done = int(((orig_len - len(suffix[1:])) / orig_len) * 100) 
    child.max_percentage = max(child.max_percentage, percentage_done)

    if len(suffix) == 1:
        child.done = True
    else:
        insert(child, suffix[1:], orig_len)
    
