import random
import string
from string import punctuation
import time
from multiprocessing import Pool
from functools import partial

punc = set(punctuation)
alphabet = list(string.ascii_uppercase)
shift = range(0,26)

def dictionary():
    with open("Dictionary.txt","r") as words:
         contents = words.read().strip().upper().split()   
    return set(contents)

def decrypting(text, shift):
    translation = get_translation(shift) #Dictionary of letters 
    decrypted = text.maketrans(translation)
    decrypted_text = text.translate(decrypted)
    return decrypted_text

def get_translation(i):
    caesar_alpha = alphabet[i:] + alphabet[:i]
    decrypt = dict(zip(caesar_alpha, alphabet))
    for k,v in decrypt.copy().items():  #This copy is used because we mutate the dictionary , otherwise we would get the error "dictionary changed size during iteration"
        decrypt[k.lower()] = v.lower()
    return decrypt

def shifting(text, text_dictionary, i):
    decrypted_text = decrypting(text,i)
    decrypted_words = "".join([i for i in decrypted_text if i not in punc]).split()
    return i, len([i for i in decrypted_words if i.upper() in text_dictionary])


if __name__ == '__main__':
    start = time.time()
    text_dictionary = dictionary()
    with open("Caesarcipher.txt",encoding="utf8") as contents:
        text = contents.read()

    multiprocessing = False
    if multiprocessing:
        with Pool(processes=None) as pool: # processes=None -> #workers = #CPUs
            all_decrypted_words = pool.imap_unordered(
                partial(shifting, text, text_dictionary),
                shift
            )
            #We dont care about the list thats why _ is used and it's not being returned
            final_shift, _ = max(all_decrypted_words, key=lambda item: item[1]) 
    else:
        all_decrypted_words = map(
            partial(shifting, text, text_dictionary),
            shift
        )
        #We dont care about the list thats why _ is used and it's not being returned
        final_shift, _ = max(all_decrypted_words, key=lambda item: item[1])

    translated_text = decrypting(text, final_shift)
    print(translated_text)
    print(final_shift)
    print(f"Execution time {time.time() - start}")

