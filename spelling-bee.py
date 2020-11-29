import json
import sys

if len(sys.argv) >= 3:
    allowed_chars = list(sys.argv[1].upper())
    required_char = sys.argv[2].upper()
    dictionary_location = sys.argv[3].lower()
else:
    raise ValueError("Please provide three strings, a list of allowed letters, a required letter, and the location of the dictionary json file.\n\nExample: dictfind.py HETNYAC Y /somepath/file")

def contains_only(word):
    letters = list(word)
    disallowed = list(filter(lambda x: x not in allowed_chars, letters))
    return len(disallowed) == 0

def has_all(word):
    f = list(filter(lambda x: x in word, allowed_chars))
    return len(f) == len(allowed_chars)

with open(dictionary_location, mode='r') as file:
    data = json.loads(file.read())
    words = data.keys()    
    words = list(filter(lambda x: len(x) >= 4 and required_char in x and contains_only(x), words))
    print(len(words))
    print(words)
    has_all = list(filter(lambda x: has_all(x), words))
    print("Has all letters: {}".format(", ".join(has_all)))
