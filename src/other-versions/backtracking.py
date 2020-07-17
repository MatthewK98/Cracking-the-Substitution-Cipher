from string import punctuation
from collections import Counter, defaultdict


def translate(text, char_mapping):
    case_sensitive_mapping = char_mapping.copy()
    for k, v in char_mapping.items():
        case_sensitive_mapping[k.upper()] = v.upper()
    return text.translate(str.maketrans(case_sensitive_mapping))


def match_pattern(cypher_word, word, char_mapping):
    "Check if cypher_word could translate into word using char_mapping"
    for cypher_letter, letter in zip(cypher_word, word):
        if cypher_letter in char_mapping:
            if char_mapping[cypher_letter] != letter:
                return False
    return True


def decrypt(text):

    def decypher_word(cypher_words):
        WORD_LEN = 6
        # Let's grab a word with a length shorter than WORD_LEN
        while True:
            if not cypher_words:
                # No more words to process. Success! \o/
                return True
            cypher_word = cypher_words.pop()
            if len(cypher_word) <= WORD_LEN:
                break

        # Get all the possible words of similar length which align with
        # the current char_mapping
        matches = [
            word for word in words[len(cypher_word)]
            if match_pattern(cypher_word, word, char_mapping)
        ]

        for match in matches:
            # Populate char_mapping
            word_mapping = dict(zip(cypher_word, match))
            # Check if new mapping does not conflict with what we
            # currently have
            word_mapping = {
                k: v for k, v in word_mapping.items() if k not in char_mapping
            }
            if set(word_mapping.values()) & set(char_mapping.values()):
                continue
            # Make a backup in case we need to backtrack.
            letters_translation_copy = char_mapping.copy()
            char_mapping.update(word_mapping)
            # We recurse
            if not decypher_word(cypher_words):
                # Dead end. Let's revert what we've done to char_mapping
                char_mapping.clear()
                char_mapping.update(letters_translation_copy)
            else:
                # We found a solution! \o/
                return True

        # No match possible, let's backtrack -> put the cypher_word back on
        # the stack and tell this was a dead end.
        cypher_words.append(cypher_word)
        return False

    cypher_words_counter = Counter(
        ''.join(c for c in text if c not in punctuation).lower().split()
    )
    # Build a frequency dictionary
    # {word_len: [words sorted by frequency]}
    words = defaultdict(list)
    with open("Dictionary.txt") as f:
        for word in f.read().splitlines():
            words[len(word)].append(word)

    char_mapping = {}

    # Sort cypher_words from least common to most common as we will use it
    # as a stack -> we will first look at the last word in the list which is
    # the most common word.
    cypher_words = sorted(cypher_words_counter, key=cypher_words_counter.get)

    if decypher_word(cypher_words):
        return char_mapping
    return None


with open("cipher.txt") as f:
    cypher_text = f.read()

trans = decrypt(cypher_text)
print(trans)
if trans:
    print(translate(cypher_text, trans))
