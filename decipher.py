import json
import pickle
import os
from xmlrpc.server import resolve_dotted_attribute

def letter_to_number(letter):
        return ord(letter) - ord('a') + 1

def load_abc(abc_filename):
    if not os.path.exists(abc_filename):
        print(f"Error: The file '{abc_filename}' does not exist.")
        return None

    with open(abc_filename, 'r') as abc_filename:
        abc_dict = dict()

        for k in range(1, 27):
            abc_dict[k] = abc_filename.readline().strip()

    return abc_dict


def load_lexicon(lexicon_filename):
    """Load the lexicon file (pickle format) into a set."""
    if not os.path.exists(lexicon_filename):
        print(f"Error: The file '{lexicon_filename}' does not exist.")
        return None

    with open(lexicon_filename, 'rb') as file:
        return set(pickle.load(file))  # Load and convert to set


def decipher_phrase(phrase, lexicon_filename, abc_filename):
    print(f'starting deciphering using {lexicon_filename} and {abc_filename}')
    if not phrase:
        result = {"status": 0, "orig_phrase": '', "K": -1}
        return result

    words_list = phrase.split() # make a words list from phrase
    split_words = [list(word) for word in words_list] # make a list of words list

    abc_dict = load_abc(abc_filename) # create a dictionary : abc are the keys and their number location are the values
    # example: a:1, b:2, c:3 ,..., x:26
    lexicon_set = load_lexicon(lexicon_filename) # set of all the words in lexicon file

    # loop for all possible k values
    for k in range(26):
        deciphered_words = []   #  make new words list with the deciphered words
        # loop for each word in phrase
        for word in split_words:
            new_word = ""  # initialize an empty string for each word
            # loop for each letter in word
            for letter in word:
                # calculate the new letter using k (in cycled manner)
                new_letter = abc_dict[(letter_to_number(letter) - k - 1) % 26 + 1]
                new_word +=  new_letter # create the full deciphered word

            # check each word if exists in lexicon
            if new_word not in lexicon_set:
                break  # next k

            deciphered_words.append(new_word)

        # happens only if all deciphered words in the list are exists in lexicon
        else:
            result = {"status": 1, "orig_phrase": " ".join(deciphered_words), "K": k}
                                                 # make a full phrase string
            return result

    # if all loop is finished and we didn't return a deciphered phrase so we can't decipher this phrase
    result = {"status": -1, "orig_phrase": '', "K": -1}
    return result



# todo: fill in your student ids
students = {'id1': '322756586', 'id2': '211449145'}

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    # note that lexicon.pkl is a serialized list of 10,000 most common English words
    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {1, -1, 0}

    if result["status"] == 1:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == -1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 0:
        print("empty phrase")
