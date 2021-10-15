# Provides functionality for mining and preprocessing the complete works of Shakespeare from Project Gutenberg
# The raw text file will be split into separate text files based on work, with header and footer information removed
# Inspiration taken from https://datawookie.dev/blog/2013/09/text-mining-the-complete-works-of-william-shakespeare/

import requests
import re
def get_raw_data() -> None:
    # Retrieves "The Project Gutenberg EBook of The Complete Works of William Shakespeare, by William Shakespeare."
    # Places raw text file containing the work in data/raw/
    url = 'https://www.gutenberg.org/cache/epub/100/pg100.txt'
    r = requests.get(url, allow_redirects=True)
    open('../data/raw.txt', 'wb').write(r.content)


def raw_to_str(raw_text: str) -> str:
    # Removes header and footer, and splits remaining text into separate text files for each work.

    # remove header and footer
    raw_text = raw_text[174:124365]
    
    # remove empty lines
    raw_text = [line for line in raw_text if line != '\n']

    # combine lines into single string
    data_str = ''.join(raw_text)

    return data_str

def split_into_works(raw_str: str) -> str:
    # Takes string.txt and splits it based on work
    # maybe this all could be done in one pass, but seems more readable this way
    works = re.split('<<[^>]*>>', raw_str)

    # remove extra newline at end for all works and any dramatis personae
    works = [work[:-1] for work in works if 'dramatis personae' not in work.lower()]

    # remove extra newline at beginning for all works except first
    for i in range(1, len(works)):
        works[i] = works[i][1:]

    return works

def remove_extra_whitespace(work: str) -> str:
    work = re.sub(' +', ' ', work)
    return work

def preprocess(raw_filepath: str ='../data/raw.txt') -> None:
    with open(raw_filepath) as f:
        raw_text_lines = f.readlines()

    raw_str = raw_to_str(raw_text_lines)
    works = split_into_works(raw_str)
    for i in range(len(works)):
        work = works[i]
        trimmed_work = remove_extra_whitespace(work)
        with open(f'../data/{i}.txt', 'w') as f:
            f.write(trimmed_work)

def get_valid_chars(folder: str ='../data/', num_works: int = 182):
    valid_chars = set()
    for i in range(num_works):
        with open(folder + f'{i}.txt') as f:
            work = f.read()
        work = set(work)
        for c in work:
            valid_chars.add(c)

    with open('../data/valid_chars.txt', 'w') as f:
        f.write(''.join(sorted(valid_chars)))
