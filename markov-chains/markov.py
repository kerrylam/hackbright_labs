"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    text_string = file.read()
    file.close()  
    return text_string

def make_chains(text_string, n):
    chains = {}
    words = text_string.split()
    words.append(None)
    # print(words)
    for i in range(len(words) - n):
        chain_key = tuple(words[i:i + n])
        chains[chain_key] = chains.get(chain_key, [])
    # if chain_key not in chains:
    #     chains[chain_key] = []
        chains[chain_key].append(words[i + n])
        # val = chains.get(chain_key, []).append(word)
        # chains[chain_key] = val
    return chains
    


# def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> chains = make_chains("hi there mary hi there juanita")

#     Each bigram (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']

#         >>> chains[('there','juanita')]
#         [None]
#     """

#     chains = {}

#     words = text_string.split()
#     words.append(None)
#     # print(words)

#     for i in range(len(words)-2):
#         chain_key = (words[i], words[i+1])

#         chains[chain_key] = chains.get(chain_key, [])

#         # if chain_key not in chains:
#         #     chains[chain_key] = []

#         chains[chain_key].append(words[i+2])

#     # print(chains)

#     return chains


def make_text(chains, n):
    """Return text from chains."""
 
    tup_key = choice(list(chains.keys()))
    while tup_key[0].istitle() is False:
        tup_key = choice(list(chains.keys()))
    words = list(tup_key)
    word = choice(chains[tup_key])
    # while word != None:

    while word[-1] not in ['.', '?', '!']:
        words.append(word)
        new_tup_key = tuple(words[-n:])
        word = choice(chains[new_tup_key])
    words.append(word)
    # new_key = (tup_key[1], word)
    return " ".join(words)


input_path = "gettysburg.txt"
# input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains, 2)

print(random_text)
