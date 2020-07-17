import string
import random
eng_alpha = list(string.ascii_lowercase)
cipher_alpha = list(string.ascii_lowercase)
random.shuffle(cipher_alpha)
char_mapping = dict(zip(tuple(eng_alpha),tuple(cipher_alpha)))

#I used this file to create decrypted tests

def results():
    txt = {}
    for k,v in char_mapping.items():
        txt[k.upper()] = v.upper()
    return txt

def make_translation():
    text_orphan = "The incredible journey of an orphaned and abandoned girl who survives life in a workhouse and eventually escapes to Canada. When she finds herself pregnant, she is banished by her employer and abandoned by her lover, so she travels alone to Newfoundland where her life takes a turn for the better."
    text_russel1 = "There are two motives for reading a book; one, that you enjoy it; the other, that you can boast about it."
    text_russel2 = "Do not fear to be eccentric in opinion, for every opinion now accepted was once eccentric."
    text_harry_potter = """October arrived, spreading a damp chill over the grounds and into the castle. Madam Pomfrey, the nurse, was kept busy by a sudden spate of colds among the staff and students. Her Pepperup potion worked instantly, though it left the drinker smoking at the ears for several hours afterward. Ginny Weasley, who had been looking pale, was bullied into taking some by Percy. The steam pouring from under her vivid hair gave the impression that her whole head was on fire.

Raindrops the size of bullets thundered on the castle windows for days on end; the lake rose, the flower beds turned into muddy streams, and Hagrid's pumpkins swelled to the size of garden sheds. Oliver Wood's enthusiasm for regular training sessions, however, was not dampened, which was why Harry was to be found, late one stormy Saturday afternoon a few days before Halloween, returning to Gryffindor Tower, drenched to the skin and splattered with mud."""
    output = ''
    for i in text_orphan.lower():
        if i in char_mapping:
            output += char_mapping[i]
        else:
            output += i
    return output
    
print(make_translation())    
print(results())
